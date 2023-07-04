from django.shortcuts import render,get_object_or_404,redirect
from aluno.models import Cidade
from .forms import CidadeForm

from aluno.models import Cidade

def cidade_listar(request):
    cidades = Cidade.objects.all()
    context = {'cidades': cidades}

    return render(request, "cidade/cidade.html",context)


def cidade_editar(request,id):
    cidade = get_object_or_404(Cidade,id=id)
   
    if request.method == 'POST':
        form = CidadeForm(request.POST,instance=cidade)

        if form.is_valid():
            form.save()
            return redirect('cidade_listar')
    else:
        form = CidadeForm(instance=cidade)

    return render(request,'cidade/form.html',{'form':form})


def cidade_remover(request, id):
    cidade = get_object_or_404(Cidade, id=id)
    cidade.delete()

    return redirect('cidade_listar')


def cidade_criar(request):
    if request.method == 'POST':
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            form = CidadeForm()
    else:
        form = CidadeForm()

    return render(request, "cidade/form.html", {'form': form})

