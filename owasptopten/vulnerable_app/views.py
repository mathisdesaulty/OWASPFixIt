import pickle
from io import BytesIO
from lxml import etree
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from vulnerable_app.models import User

def vulnerable_function(request):
    return render(request, 'accueil_vulnerable.html')

def sql_injection_vulnerable(request):
    results = []
    query = ""
    
    if request.method == 'POST':
        search_query = request.POST.get('search', '')
        query = f"SELECT * FROM fixed_app_product WHERE name LIKE '{search_query}'"
        
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
    
    return render(request, 'sql_injection_vulnerable.html', {'results': results, 'query': query})

def xss_vulnerable(request):
    comment = "" 

    # Retrieve the comment from URL parameters
    if request.method == 'POST':
        comment = request.POST.get('comment', '') 
    else:
        comment = request.GET.get('comment', '')

    return render(request, 'xss_vulnerable.html', {'comment': comment})

def sensitive_data_vulnerable(request):
    return render(request, 'sensitive_data_vulnerable.html')

def sensitive_data_exposure(request):
    # Retrieve all users from the database
    users = User.objects.all()

    # Log the number of users retrieved (for debugging)
    print(f"Number of users retrieved: {users.count()}")

    # If the list is empty, add a message to check
    if not users.exists():
        return JsonResponse({"error": "No users found"}, status=404)

    # Format user data for JSON display
    user_data = [{"username": user.username, "password": user.password} for user in users]

    # Log user data (for debugging)
    print(f"User data: {user_data}")

    # Return a JSON response with user data
    return JsonResponse(user_data, safe=False)

def upload_xml_vulnerable(request):
    if request.method == 'POST' and request.FILES.get('xmlfile'):
        xml_file = request.FILES['xmlfile']
        try:
            # Read the content of the uploaded file
            xml_content = xml_file.read()

            # Create an XML parser vulnerable to XXE
            parser = etree.XMLParser(load_dtd=True, no_network=False)  # Enable external entities
            tree = etree.parse(BytesIO(xml_content), parser)  # Parse the file content
            root = tree.getroot()

            # Return the parsed XML content or external entity
            return HttpResponse(f'XML Parsed Successfully: {etree.tostring(root)}')

        except etree.XMLSyntaxError as e:
            return HttpResponse(f"An error occurred: {str(e)}", status=400)

    return render(request, 'upload_xml.html')

def insecure_deserialization_vulnerable(request):
    if request.method == 'POST' and request.FILES.get('picklefile'):
        pickle_file = request.FILES['picklefile']
        try:
            # Load data without verification
            data = pickle.load(pickle_file)
            return HttpResponse(f'Pickle data processed: {data}')

        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}", status=500)

    return render(request, 'insecure_deserialization_vulnerable.html')
