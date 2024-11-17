
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    path('cadastrar-medico/', views.CadastroMedicoView.as_view(), name='cadastrar_medico'),
    path('dashboard-medico/', views.DashboardMedicoView.as_view(), name='dashboard_medico')


]
