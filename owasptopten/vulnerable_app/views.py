from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

def vulnerable_function(request):
    return render(request, 'accueil_vulnerable.html')

def home(request):
    return render(request, 'accueil_choice.html')

def sql_injection_vulnerable(request):
    return render(request, 'sql_injection_vulnerable.html')

def xss_vulnerable(request):
    return render(request, 'xss_vulnerable.html')

def sensitive_data_vulnerable(request):
    return render(request, 'sensitive_data_vulnerable.html')

def auth_vulnerable(request):
    return render(request, 'auth_vulnerable.html')

def config_vulnerable(request):
    return render(request, 'config_vulnerable.html')