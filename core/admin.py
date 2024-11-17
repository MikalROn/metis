from django.contrib import admin
from .models import Usuario, Medico, Paciente, Medicacao, Prontuario, Consulta

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'cpf', 'telefone', 'tipo_usuario')
    search_fields = ('username', 'cpf')

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('usuario_display', 'especialidade', 'crm')  # Alterado para método
    search_fields = ('usuario__username', 'crm')

    def usuario_display(self, obj):
        return obj.usuario.username  # Acessando o campo 'username' do usuário relacionado
    usuario_display.short_description = 'Medico'

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('usuario_display', 'data_nascimento')  # Alterado para método
    search_fields = ('usuario__username',)

    def usuario_display(self, obj):
        return obj.usuario.username  # Acessando o campo 'username' do usuário relacionado
    usuario_display.short_description = 'Paciente'

class MedicacaoAdmin(admin.ModelAdmin):
    list_display = ('data_validade', 'horario', 'dosagem', 'agenda')

class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data', 'arquivo')

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data', 'horario', 'especialidade')

# Registrando as classes no admin
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medicacao, MedicacaoAdmin)
admin.site.register(Prontuario, ProntuarioAdmin)
admin.site.register(Consulta, ConsultaAdmin)
