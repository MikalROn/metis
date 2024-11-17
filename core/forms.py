from django import forms
from django.contrib.auth import get_user_model
from .models import Medico, Paciente, Medicacao, Prontuario, Receita, Consulta


class MedicoLoginForm(forms.Form):
    cpf = forms.CharField(max_length=11, label='CPF')
    crm = forms.CharField(max_length=20, label='CRM')
    senha = forms.CharField(widget=forms.PasswordInput(), label='Senha')

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['cpf', 'nome', 'especialidade', 'crm', 'password']  # Campos a serem exibidos
        widgets = {
            'password': forms.PasswordInput(),  # Exibir o campo de senha como senha
        }
    
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def save(self, commit=True):
        medico = super().save(commit=False)
        medico.set_password(self.cleaned_data['password'])  # Configurar a senha criptografada
        if commit:
            medico.save()
        return medico

class PacienteLoginForm(forms.Form):
    cpf = forms.CharField(max_length=11, label='CPF')
    email = forms.EmailField(label='Email')
    senha = forms.CharField(widget=forms.PasswordInput(), label='Senha')
    
    
# Formulário de medicação (Medicacao)
class MedicacaoForm(forms.ModelForm):
    class Meta:
        model = Medicacao
        fields = ['data_validade', 'horario', 'dosagem', 'agenda', 'receita']
        widgets = {
            'data_validade': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicionando placeholders aos campos
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

# Formulário de prontuário (Prontuario)
class ProntuarioForm(forms.ModelForm):
    class Meta:
        model = Prontuario
        fields = ['paciente', 'medico', 'arquivo', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicionando placeholders aos campos
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

# Formulário de receita (Receita)
class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['paciente', 'medico', 'data_emissao', 'descricao', 'documento']
        widgets = {
            'data_emissao': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicionando placeholders aos campos
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

# Formulário de consulta (Consulta)
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'data', 'horario', 'especialidade']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicionando placeholders aos campos
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
