import jsonpickle
from defusedxml.lxml import fromstring
from lxml import etree
from django.contrib.sessions.models import Session
from datetime import timezone
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.html import escape
from .models import Product
from django.db import connection
import re
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import User

def accueil(request):
    return render(request, 'accueil_fixed.html')

def sql_injection_fixed(request):
    results = []
    search_query = ""  

    if request.method == 'POST':
        search_query = request.POST.get('search', '')
        
        if re.search(r"[;'\"]", search_query):
            return HttpResponse("Invalid search query!")

        query = "SELECT * FROM fixed_app_product WHERE name LIKE %s"
        
        with connection.cursor() as cursor:
            cursor.execute(query, [f'%{search_query}%'])
            results = cursor.fetchall()

    return render(request, 'sql_injection_fixed.html', {'results': results, 'query': search_query})  

def xss_fixed(request):
    comment = "" 

    if request.method == 'POST':
        comment = request.POST.get('comment', '') 
        
    return render(request, 'xss_fixed.html', {'comment': comment})

def sensitive_data_fixed(request):
    return render(request, 'sensitive_data_fixed.html')

def upload_xml_fixed(request):
    if request.method == 'POST' and request.FILES.get('xmlfile'):
        xml_file = request.FILES['xmlfile']
        try:
            # Read the content of the uploaded file
            xml_content = xml_file.read()

            # Use defusedxml to parse the XML safely
            root = fromstring(xml_content)  # We do not call getroot() here

            # Get the content of the element
            response_content = etree.tostring(root, encoding='unicode')  # Convert the element to a string

            return HttpResponse(f'XML Parsed Successfully: {response_content}')

        except Exception as e:
            return HttpResponse(f"Error parsing XML: {str(e)}", status=400)

    return render(request, 'upload_xml_fixed.html')

def insecure_deserialization_fixed(request):
    if request.method == 'POST' and request.FILES.get('jsonfile'):
        json_file = request.FILES['jsonfile']
        try:
            # Read the content of the uploaded file
            json_content = json_file.read().decode('utf-8')

            # Deserialize the JSON content
            data = jsonpickle.decode(json_content)
            
            # Process the deserialized data
            return HttpResponse(f'JSON Data Processed: {data}')

        except jsonpickle.JsonPickleException as e:
            return HttpResponse(f"An error occurred: {str(e)}", status=400)
        except Exception as e:
            return HttpResponse(f"An error occurred while processing: {str(e)}", status=500)
    return render(request, 'insecure_deserialization_fixed.html')

@login_required(login_url='/login/')
def sensitive_data_exposure(request):
    if not request.user.is_superuser:
        # If the user is not an admin, raise a PermissionDenied exception
        raise PermissionDenied("You must be an administrator to access this page.")

    # Retrieve all users from the database
    users = User.objects.all()

    # If the list is empty, add a message to check
    if not users.exists():
        return JsonResponse({"error": "No users found"}, status=404)

    # Format user data for JSON display
    user_data = [{"username": user.username, "password": user.password} for user in users]
    
    return JsonResponse(user_data, safe=False)
