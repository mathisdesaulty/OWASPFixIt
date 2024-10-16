from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vulnerable_app.urls')),  # Redirige vers les URLs de l'application vulnérable
    path('fixed/', include('fixed_app.urls')),  # Redirige vers les URLs de l'application corrigée
]
