from django.urls import path
from .views import accueil, vulnerable_function

urlpatterns = [
    path('', accueil, name='vulnerable_accueil'),
    path('vulnerable/', vulnerable_function, name='vulnerable_function'),
]