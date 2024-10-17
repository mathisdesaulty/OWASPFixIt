from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape
from .models import Product


def accueil(request):
    return render(request, 'accueil_fixed.html')

def fixed_function(request):
    user_input = request.GET.get('input', '')
    # Correction : échappe l'entrée utilisateur
    safe_input = escape(user_input)
    return HttpResponse(f"Tu as entré : {safe_input}")

def sql_injection_fixed(request):
    return render(request, 'sql_injection_fixed.html')

def xss_fixed(request):
    return render(request, 'xss_fixed.html')

def sensitive_data_fixed(request):
    return render(request, 'sensitive_data_fixed.html')

def auth_fixed(request):
    return render(request, 'auth_fixed.html')

def config_fixed(request):
    return render(request, 'config_fixed.html')
