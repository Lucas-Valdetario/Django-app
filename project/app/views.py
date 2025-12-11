from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import AppModel
from .forms import tarefaForm
from django.http import HttpRequest

# Create your views here.
class GerenciadorTarefasViews:
    def tarefas_home(self, request):
        context = {
            "tarefas": AppModel.objects.all()
        }
        return render(request, 'tarefas/home.html', context)

    def tarefas_adicionar(self, request: HttpRequest):
        if request.method == 'POST':
            formulario = tarefaForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                return redirect("home")

        context = {
            "form": tarefaForm()
        }
        return render(request, 'tarefas/adicionar.html', context)

    def tarefas_remover(self, request: HttpRequest, id: int):
        if request.method == 'POST':
            ids_tarefas = request.POST.getlist("tarefas")
            AppModel.objects.filter(id__in=ids_tarefas).delete()
            return redirect("home")

        context = {
            "tarefas": AppModel.objects.all()
        }
        return render(request, 'tarefas/remover.html', context)
