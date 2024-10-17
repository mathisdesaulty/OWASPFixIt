# fixed_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='fixed_accueil'),
    path('sql-injection/', views.sql_injection_fixed, name='sql_injection_fixed'),
    path('xss/', views.xss_fixed, name='xss_fixed'),
    path('sensitive-data/', views.sensitive_data_fixed, name='sensitive_data_fixed'),
    path('auth/', views.auth_fixed, name='auth_fixed'),
    path('config/', views.config_fixed, name='config_fixed'),
]
