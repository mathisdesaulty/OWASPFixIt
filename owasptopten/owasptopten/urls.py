from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),  # Inclut les URL de connexion
    path('', views.home, name="home"),  # Redirige vers les URLs de l'application corrigée
    path('vulnerable/', include('vulnerable_app.urls')),  # Redirige vers les URLs de l'application vulnérable
    path('fixed/', include('fixed_app.urls')),  # Redirige vers les URLs de l'application corrigée
    
]
