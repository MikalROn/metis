from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


# Views for Consulta
def consulta_list(request):
    return ...


def consulta_detail(request, pk):
    return ...

def consulta_create(request):
    return ...

def consulta_update(request, pk):
    return ...

def consulta_delete(request, pk):
    return ...

# Views for Paciente
def paciente_list(request):
    return ...

def paciente_detail(request, pk):
    return ...

def paciente_create(request):
    return ...

def paciente_update(request, pk):
    return ...

def paciente_delete(request, pk):
    return ...

# Views for Prontuario
def prontuario_list(request):
    return ...

def prontuario_detail(request, pk):
    return ...

def prontuario_create(request):
    return ...

def prontuario_update(request, pk):
    return ...

def prontuario_delete(request, pk):
    return ...

# Views for Receita
def receita_list(request):
    return ...

def receita_detail(request, pk):
    return ...

def receita_create(request):
    return ...

def receita_update(request, pk):
    return ...

def receita_delete(request, pk):
    return ...

# Views for Medico
def medico_list(request):
    return ...

def medico_detail(request, pk):
    return ...

def medico_create(request):
    return ...

def medico_update(request, pk):
    return ...

def medico_delete(request, pk):
    return ...