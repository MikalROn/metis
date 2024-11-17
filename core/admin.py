from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Medico

class UsuarioAdmin(UserAdmin):
    model = Usuario
    # Personaliza os campos que aparecerão no formulário de edição
    fieldsets = (
        (None, {'fields': ('cpf', 'nome', 'password')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    # Campos a serem exibidos na lista do Admin
    list_display = ('cpf', 'nome', 'is_staff', 'is_active')

    # Oculta os campos desnecessários
    exclude = ('last_login', 'date_joined', 'groups', 'user_permissions')

    # Define como o campo de senha será tratado
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'nome', 'password1', 'password2'),
        }),
    )

    # Corrigir a ordenação para um campo válido, como 'cpf'
    ordering = ('cpf',)  # Ordenando pelo campo 'cpf'

# Registrando o modelo Usuario com o administrador personalizado
admin.site.register(Usuario, UsuarioAdmin)

# Registrando o modelo Medico para o Admin
@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'especialidade', 'crm')
    search_fields = ('nome', 'cpf', 'crm')
    ordering = ('crm',)  # Ordenando pelo campo 'crm'
    
    exclude = ('last_login', 'date_joined', 'groups', 'user_permissions')