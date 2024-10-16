from django.http import HttpResponse
from django.shortcuts import render

def accueil(request):
    return HttpResponse("Bienvenue sur la version vulnérable du site !")

def vulnerable_function(request):
    user_input = request.GET.get('input', '')
    # Exemple de faille : injection SQL
    # Imaginons que tu interroges la base de données ici sans validation
    return HttpResponse(f"Tu as entré : {user_input}")



def home(request):
    return render(request, 'accueil_choice.html')
