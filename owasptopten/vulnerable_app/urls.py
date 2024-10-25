from django.urls import path
from . import views

urlpatterns = [
    path('', views.vulnerable_function, name='vulnerable_function'),
    path('sql-injection/', views.sql_injection_vulnerable, name='sql_injection_vulnerable'),
    path('xss/', views.xss_vulnerable, name='xss_vulnerable'),
    path('sensitive-data/', views.sensitive_data_vulnerable, name='sensitive_data_vulnerable'),
    path('upload_xml_vulnerable/', views.upload_xml_vulnerable, name='upload_xml_vulnerable'),
    path('insecure_deserialization_vulnerable/', views.insecure_deserialization_vulnerable, name='insecure_deserialization_vulnerable'),
    path('sensitive-data-exposure/', views.sensitive_data_exposure, name='sensitive_data_exposure'),
]