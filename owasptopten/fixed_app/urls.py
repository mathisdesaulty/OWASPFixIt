from django.urls import path
from .views import accueil, fixed_function

urlpatterns = [
    path('', accueil, name='fixed_accueil'),
    path('fixed/', fixed_function, name='fixed_function'),
]
