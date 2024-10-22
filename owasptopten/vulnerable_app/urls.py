from django.urls import path
from . import views

urlpatterns = [
    path('', views.vulnerable_function, name='vulnerable_function'),
    path('sql-injection/', views.sql_injection_vulnerable, name='sql_injection_vulnerable'),
    path('xss/', views.xss_vulnerable, name='xss_vulnerable'),
    path('sensitive-data/', views.sensitive_data_vulnerable, name='sensitive_data_vulnerable'),
    path('auth/', views.auth_vulnerable, name='auth_vulnerable'),
    path('config/', views.config_vulnerable, name='config_vulnerable'),
    path('sensitive-data-exposure/', views.sensitive_data_exposure, name='sensitive_data_exposure'),
]