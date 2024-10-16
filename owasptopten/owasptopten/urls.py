from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vulnerable/', include('vulnerable_app.urls')),
    path('fixed/', include('fixed_app.urls')),
]
