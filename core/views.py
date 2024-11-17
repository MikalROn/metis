from django.shortcuts import render, redirect
from django.views.generic import (
 ListView, DetailView, CreateView, UpdateView, DeleteView, View, TemplateView
)
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Consulta, Paciente, Prontuario, Medico, Medicacao
from django.contrib import messages
from .forms import MedicoLoginForm, PacienteLoginForm, MedicoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'home.html')

@method_decorator(login_required, name='dispatch')
class DashboardMedicoView(TemplateView):
    template_name = 'dashboard_medico.html'
    
    def dispatch(self, request, *args, **kwargs):
       
        if not hasattr(request.user, 'medico'): 
            return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
        return super().dispatch(request, *args, **kwargs)
     

class CadastroMedicoView(SuccessMessageMixin, CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/cadastrar_medico.html'
    success_url = reverse_lazy('cadastrar_medioco')  
    success_message = "Médico cadastrado com sucesso!"

    def form_valid(self, form):
        """Configurar a senha do médico antes de salvar."""
        medico = form.save(commit=False)
        medico.set_password(form.cleaned_data['password'])
        medico.save()
        return super().form_valid(form)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)  # Desconecta o usuário
        return redirect('home')  # Redireciona para a página inicial ou outra página após logout

class LoginView(View):
    def get(self, request, *args, **kwargs):
        medico_form = MedicoLoginForm()
        paciente_form = PacienteLoginForm()
        return render(request, 'login.html', {
            'medico_form': medico_form,
            'paciente_form': paciente_form,
        })

    def post(self, request, *args, **kwargs):
        medico_form = MedicoLoginForm(request.POST)
        paciente_form = PacienteLoginForm(request.POST)

        # Verifica se o formulário do médico é válido
        if medico_form.is_valid():
            cpf = medico_form.cleaned_data['cpf']
            senha = medico_form.cleaned_data['senha']
            # Autenticação do médico
            usuario = authenticate(request, cpf=cpf, password=senha)
            login(request, usuario)
            return redirect('dashboard_medico')
        
        elif paciente_form.is_valid():
            cpf = paciente_form.cleaned_data['cpf']
            senha = paciente_form.cleaned_data['senha']
            # Autenticação do paciente
            usuario = authenticate(request, cpf=cpf, password=senha)
            login(request, usuario)
            return redirect('dashboard_paciente')

        # Caso nenhum formulário seja válido, renderiza novamente a página com os erros
        return render(request, 'login.html', {
            'medico_form': medico_form,
            'paciente_form': paciente_form,
        })

################################
# CONSULTA 
###############################
class ConsultaListView(ListView):
    model = Consulta
    template_name = 'consulta_list.html'

class ConsultaDetailView(DetailView):
    model = Consulta
    template_name = 'consulta_detail.html'

class ConsultaCreateView(CreateView):
    model = Consulta
    fields = '__all__'  # Ou especifique os campos desejados
    template_name = 'consulta_form.html'
    success_url = reverse_lazy('consulta_list')

class ConsultaUpdateView(UpdateView):
    model = Consulta
    fields = '__all__'
    template_name = 'consulta_form.html'
    success_url = reverse_lazy('consulta_list')

class ConsultaDeleteView(DeleteView):
    model = Consulta
    template_name = 'consulta_confirm_delete.html'
    success_url = reverse_lazy('consulta_list')

################################
# Paciente 
###############################
class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente_list.html'

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'paciente_detail.html'

class PacienteCreateView(CreateView):
    model = Paciente
    fields = '__all__'
    template_name = 'paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = '__all__'
    template_name = 'paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'paciente_confirm_delete.html'
    success_url = reverse_lazy('paciente_list')

################################
# Prontuário
###############################
class ProntuarioListView(ListView):
    model = Prontuario
    template_name = 'prontuario_list.html'

class ProntuarioDetailView(DetailView):
    model = Prontuario
    template_name = 'prontuario_detail.html'

class ProntuarioCreateView(CreateView):
    model = Prontuario
    fields = '__all__'
    template_name = 'prontuario_form.html'
    success_url = reverse_lazy('prontuario_list')

class ProntuarioUpdateView(UpdateView):
    model = Prontuario
    fields = '__all__'
    template_name = 'prontuario_form.html'
    success_url = reverse_lazy('prontuario_list')

class ProntuarioDeleteView(DeleteView):
    model = Prontuario
    template_name = 'prontuario_confirm_delete.html'
    success_url = reverse_lazy('prontuario_list')

################################
# Médico 
###############################
class MedicoListView(ListView):
    model = Medico
    template_name = 'medico_list.html'

class MedicoDetailView(DetailView):
    model = Medico
    template_name = 'medico_detail.html'

class MedicoCreateView(CreateView):
    model = Medico
    fields = '__all__'
    template_name = 'medico_form.html'
    success_url = reverse_lazy('medico_list')

class MedicoUpdateView(UpdateView):
    model = Medico
    fields = '__all__'
    template_name = 'medico_form.html'
    success_url = reverse_lazy('medico_list')

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'medico_confirm_delete.html'
    success_url = reverse_lazy('medico_list')

class MedicacaoListView(ListView):
    model = Medicacao
    template_name = 'medicacao/medicacao_list.html'
    context_object_name = 'medicacoes'

class MedicacaoDetailView(DetailView):
    model = Medicacao
    template_name = 'medicacao/medicacao_detail.html'

class MedicacaoCreateView(CreateView):
    model = Medicacao
    fields = ['data_validade', 'horario', 'dosagem', 'agenda', 'receita']
    template_name = 'medicacao/medicacao_form.html'
    success_url = reverse_lazy('medicacao_list')

class MedicacaoUpdateView(UpdateView):
    model = Medicacao
    fields = ['data_validade', 'horario', 'dosagem', 'agenda', 'receita']
    template_name = 'medicacao/medicacao_form.html'
    success_url = reverse_lazy('medicacao_list')

class MedicacaoDeleteView(DeleteView):
    model = Medicacao
    template_name = 'medicacao/medicacao_confirm_delete.html'
    success_url = reverse_lazy('medicacao_list')