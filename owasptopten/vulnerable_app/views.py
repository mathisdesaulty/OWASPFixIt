from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
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



def sensitive_data_exposure(request):
    # Récupérer tous les utilisateurs depuis la base de données
    users = User.objects.all()

    # Journaliser le nombre d'utilisateurs récupérés (pour déboguer)
    print(f"Nombre d'utilisateurs récupérés : {users.count()}")

    # Si la liste est vide, ajouter un message pour vérifier
    if not users.exists():
        return JsonResponse({"error": "No users found"}, status=404)

    # Formatage des données utilisateur pour l'affichage JSON
    user_data = [{"username": user.username, "password": user.password} for user in users]

    # Journaliser les données utilisateur (pour déboguer)
    print(f"Données utilisateur : {user_data}")

    # Retourner une réponse JSON avec les données des utilisateurs
    return JsonResponse(user_data, safe=False)

def auth_vulnerable(request):
    return render(request, 'auth_vulnerable.html')

def config_vulnerable(request):
    return render(request, 'config_vulnerable.html')