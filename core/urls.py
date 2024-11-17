
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # CRUD URLs for Consulta
    path('consulta/', views.consulta_list, name='consulta_list'),
    path('consulta/<int:pk>/', views.consulta_detail, name='consulta_detail'),
    path('consulta/add/', views.consulta_create, name='consulta_create'),
    path('consulta/<int:pk>/edit/', views.consulta_update, name='consulta_update'),
    path('consulta/<int:pk>/delete/', views.consulta_delete, name='consulta_delete'),

    # CRUD URLs for Paciente
    path('paciente/', views.paciente_list, name='paciente_list'),
    path('paciente/<int:pk>/', views.paciente_detail, name='paciente_detail'),
    path('paciente/add/', views.paciente_create, name='paciente_create'),
    path('paciente/<int:pk>/edit/', views.paciente_update, name='paciente_update'),
    path('paciente/<int:pk>/delete/', views.paciente_delete, name='paciente_delete'),

    # CRUD URLs for Prontuario
    path('prontuario/', views.prontuario_list, name='prontuario_list'),
    path('prontuario/<int:pk>/', views.prontuario_detail, name='prontuario_detail'),
    path('prontuario/add/', views.prontuario_create, name='prontuario_create'),
    path('prontuario/<int:pk>/edit/', views.prontuario_update, name='prontuario_update'),
    path('prontuario/<int:pk>/delete/', views.prontuario_delete, name='prontuario_delete'),

    # CRUD URLs for Receita
    path('receita/', views.receita_list, name='receita_list'),
    path('receita/<int:pk>/', views.receita_detail, name='receita_detail'),
    path('receita/add/', views.receita_create, name='receita_create'),
    path('receita/<int:pk>/edit/', views.receita_update, name='receita_update'),
    path('receita/<int:pk>/delete/', views.receita_delete, name='receita_delete'),

    # CRUD URLs for Medico
    path('medico/', views.medico_list, name='medico_list'),
    path('medico/<int:pk>/', views.medico_detail, name='medico_detail'),
    path('medico/add/', views.medico_create, name='medico_create'),
    path('medico/<int:pk>/edit/', views.medico_update, name='medico_update'),
    path('medico/<int:pk>/delete/', views.medico_delete, name='medico_delete')
]
