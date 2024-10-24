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
    search_query = ""  # Initialize search_query as an empty string

    if request.method == 'POST':
        search_query = request.POST.get('search', '')
        
        # Validation simple pour éviter les injections SQL
        if re.search(r"[;'\"]", search_query):
            return HttpResponse("Invalid search query!")

        query = "SELECT * FROM fixed_app_product WHERE name LIKE %s"
        
        with connection.cursor() as cursor:
            cursor.execute(query, [f'%{search_query}%'])
            results = cursor.fetchall()

    return render(request, 'sql_injection_fixed.html', {'results': results, 'query': search_query})  # Pass search_query instead of the SQL query

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
            # Lire le contenu du fichier uploadé
            xml_content = xml_file.read()

            # Utiliser defusedxml pour parser le XML en toute sécurité
            root = fromstring(xml_content)  # On ne fait pas appel à getroot() ici

            # Récupérer le contenu de l'élément
            response_content = etree.tostring(root, encoding='unicode')  # Convertir l'élément en chaîne

            return HttpResponse(f'XML Parsed Successfully: {response_content}')

        except etree.XMLSyntaxError as e:
            return HttpResponse(f"etree.XMLSyntaxError error occurred: {str(e)}", status=400)
        except Exception as e:
            return HttpResponse(f"Usage of malicious XML", status=500)

    return render(request, 'upload_xml_fixed.html')

def config_fixed(request):
    return render(request, 'config_fixed.html')

@login_required(login_url='/login/')
def sensitive_data_exposure(request):
    if not request.user.is_superuser:
        # Si l'utilisateur n'est pas admin, on renvoie une exception de type PermissionDenied
        raise PermissionDenied("Vous devez être un administrateur pour accéder à cette page.")

    # Récupération de tous les utilisateurs dans la base de données
    users = User.objects.all()

    # Si la liste est vide, ajouter un message pour vérifier
    if not users.exists():
        return JsonResponse({"error": "No users found"}, status=404)

    # Formatage des données utilisateur pour l'affichage JSON
    user_data = [{"username": user.username, "password": user.password} for user in users]
    
    return JsonResponse(user_data, safe=False)