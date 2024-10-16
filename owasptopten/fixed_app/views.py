from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape

def accueil(request):
    return HttpResponse("Bienvenue sur la version corrigée du site !")

def fixed_function(request):
    user_input = request.GET.get('input', '')
    # Correction : échappe l'entrée utilisateur
    safe_input = escape(user_input)
    return HttpResponse(f"Tu as entré : {safe_input}")
