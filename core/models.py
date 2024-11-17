from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Usuario(AbstractUser):
    # Campos adicionais para todos os usuários
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)

    # Tipo de usuário (opcional, pode usar os grupos do Django também)
    TIPO_USUARIO_CHOICES = (
        ('medico', 'Médico'),
        ('paciente', 'Paciente'),
    )
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)

    # Relacionamento com grupos e permissões
    groups = models.ManyToManyField(Group, related_name="usuario_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuario_permissions", blank=True)

    def save(self, *args, **kwargs):
        # Adicionar o usuário ao grupo correspondente automaticamente
        if not self.pk:  # Apenas ao criar
            if self.tipo_usuario == 'medico':
                grupo, _ = Group.objects.get_or_create(name='Medico')
                self.groups.add(grupo)
            elif self.tipo_usuario == 'paciente':
                grupo, _ = Group.objects.get_or_create(name='Paciente')
                self.groups.add(grupo)
        super().save(*args, **kwargs)


class Medico(Usuario):
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True)


class Paciente(Usuario):
    data_nascimento = models.DateField()


class Medicacao(models.Model):
    data_validade = models.DateField()
    horario = models.TimeField()
    dosagem = models.CharField(max_length=50)
    agenda = models.CharField(max_length=100)
    receita = models.FileField(upload_to='receitas/')


class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="prontuarios")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="prontuarios")
    arquivo = models.FileField(upload_to='prontuarios/')
    data = models.DateField()


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="consultas")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="consultas")
    data = models.DateField()
    horario = models.TimeField()
    especialidade = models.CharField(max_length=100)