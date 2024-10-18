from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape
from .models import Product
from django.db import connection
import re

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

def auth_fixed(request):
    return render(request, 'auth_fixed.html')

def config_fixed(request):
    return render(request, 'config_fixed.html')
