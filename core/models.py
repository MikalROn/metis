from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Gerenciador personalizado para o modelo Usuario.
    Usa CPF como identificador único para autenticação.
    """
    def create_user(self, cpf, password=None, **extra_fields):
        if not cpf:
            raise ValueError("O campo CPF é obrigatório.")
        extra_fields.setdefault('is_active', True)
        user = self.model(cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuários precisam ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuários precisam ter is_superuser=True.')

        return self.create_user(cpf, password, **extra_fields)


class Usuario(AbstractUser):
    username = None  # Remove o campo padrão de username
    first_name = None  # Remove o primeiro nome
    last_name = None  # Remove o sobrenome

    # Campos personalizados
    cpf = models.CharField(
        max_length=11,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("CPF")
    )
    nome = models.CharField(max_length=100, verbose_name=_("Nome"))

    # Relacionamento com grupos e permissões
    groups = models.ManyToManyField(Group, related_name="usuario_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuario_permissions", blank=True)

    # Configuração do gerenciador
    objects = CustomUserManager()

    USERNAME_FIELD = 'cpf'  # CPF será usado como identificador único
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.cpf})"


class Medico(Usuario):
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True)
    
    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
    
    def __str__(self):
        return self.nome


class Paciente(Usuario):
    data_nascimento = models.DateField()
    medico_responsavel = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        related_name="pacientes",  # Nome único para evitar conflito
        verbose_name=_("Médico responsável")
    )


class Medicacao(models.Model):
    data_validade = models.DateField(verbose_name="Data de Validade")
    horario = models.TimeField(verbose_name="Horário")
    dosagem = models.CharField(max_length=100, verbose_name="Dosagem")
    data_agendada = models.DateField(verbose_name="Data Agendada")
    receita = models.FileField(upload_to='receitas/', null=True, blank=True)

    def __str__(self):
        return f"{self.dosagem} - {self.horario} (Validade: {self.data_validade})"


class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="prontuarios")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="prontuarios")
    arquivo = models.FileField(upload_to='prontuarios/')
    data = models.DateField()


class Receita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="receitas")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="receitas")
    data_emissao = models.DateField()
    descricao = models.TextField()
    documento = models.FileField(upload_to='receitas/')


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="consultas")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="consultas")
    data = models.DateField()
    horario = models.TimeField()
    especialidade = models.CharField(max_length=100)
