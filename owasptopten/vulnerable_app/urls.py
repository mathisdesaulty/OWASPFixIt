from django.urls import path
from .views import home, accueil,vulnerable_function

urlpatterns = [
    path('', home, name='vulnerable_accueil'),  # Page d'accueil vulnérable
    path('vulnerable/',accueil , name='vulnerable_function'),  # Autres URLs vulnérables
]
