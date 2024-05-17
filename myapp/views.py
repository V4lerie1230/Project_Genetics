from django.shortcuts import render
from .models import Mutation


def mi_vista(request):
    return render(request, 'myapp/home.html')
    

def listar_mutations(request):
    mutations = Mutation.objects.all()
    return render(request, 'myapp/listar_mutations.html', {'mutations': mutations})