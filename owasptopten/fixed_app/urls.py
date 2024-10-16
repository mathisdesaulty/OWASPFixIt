from django.urls import path
from .views import accueil, fixed_function

urlpatterns = [
    path('', accueil, name='fixed_accueil'),  # Page d'accueil corrigée
    path('fixed/', fixed_function, name='fixed_function'),  # Autres URLs corrigées
]
