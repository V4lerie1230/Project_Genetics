from django.shortcuts import render
from .models import Mutation, Diseases, Crossing


def mi_vista(request):
    return render(request, 'myapp/home.html')
    

def listar_mutations(request):
    mutations = Mutation.objects.all()
    return render(request, 'myapp/listar_mutations.html', {'mutations': mutations})

def listar_diseases(request):
    diseases = Diseases.objects.all()
    return render(request, 'myapp/listar_diseases.html', {'diseases': diseases})

def listar_crossing(request):
    crossing = Crossing.objects.all()
    return render(request, 'myapp/listar_crossing.html', {'crossing': crossing})
 