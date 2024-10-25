# fixed_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.accueil, name='fixed_accueil'),
    path('sql-injection/', views.sql_injection_fixed, name='sql_injection_fixed'),
    path('xss/', views.xss_fixed, name='xss_fixed'),
    path('sensitive-data/', views.sensitive_data_fixed, name='sensitive_data_fixed'),
    path('upload_xml_fixed/', views.upload_xml_fixed, name='upload_xml_fixed'),
    path('insecure_deserialization_fixed/', views.insecure_deserialization_fixed, name='insecure_deserialization_fixed'),
    path('sensitive-data-exposure/', views.sensitive_data_exposure, name='sensitive_data_exposure'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout-user/<int:user_id>/', views.logout_user, name='logout_user'),

    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),



]
