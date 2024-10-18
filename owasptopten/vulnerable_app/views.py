from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

def vulnerable_function(request):
    return render(request, 'accueil_vulnerable.html')

def home(request):
    return render(request, 'accueil_choice.html')

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

from django.shortcuts import render

def xss_vulnerable(request):
    comment = "" 

    # Récupérer le commentaire depuis les paramètres d'URL
    if request.method == 'POST':
        comment = request.POST.get('comment', '') 
    else:
        comment = request.GET.get('comment', '')

    return render(request, 'xss_vulnerable.html', {'comment': comment})


def sensitive_data_vulnerable(request):
    return render(request, 'sensitive_data_vulnerable.html')

def auth_vulnerable(request):
    return render(request, 'auth_vulnerable.html')

def config_vulnerable(request):
    return render(request, 'config_vulnerable.html')