
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    path('cadastrar-medico/', views.CadastroMedicoView.as_view(), name='cadastrar_medico'),
    path('dashboard-medico/', views.DashboardMedicoView.as_view(), name='dashboard_medico'),

    # crud paciente
    path('paciente', views.PacienteListView.as_view(), name='paciente_list'),
    path('paciente/novo/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('paciente/<int:pk>/', views.PacienteDetailView.as_view(), name='paciente_detail'),
    path('paciente/<int:pk>/editar/', views.PacienteUpdateView.as_view(), name='paciente_update'),
    path('paciente/<int:pk>/excluir/', views.PacienteDeleteView.as_view(), name='paciente_delete'),


]
