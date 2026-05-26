import collections
from django import shortcuts
from django import shortcuts
from django import shortcuts
from django import shortcuts
from django import shortcuts
from django import shortcuts
from django import shortcuts
from django import shortcuts
from django import shortcuts
from django import shortcuts
from django import shortcuts
from django import shortcuts
from django import contrib
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ocorrencia
from .forms import OcorrenciaForm

def cadastrar(request):
    if request.method == "POST":
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ocorrência cadastrada com sucesso!")
            return redirect("listar")
    else:
        form = OcorrenciaForm()

    return render(request, "ocorrencias/cadastrar.html", {"form": form})

def listar(request):
    ocorrencias = Ocorrencia.objects.all()

    # Busca por nome
    nome = request.GET.get("nome")
    if nome:
        ocorrencias = ocorrencias.filter(nome_aluno__icontains=nome)

    # Busca por curso
    curso = request.GET.get("curso")
    if curso:
        ocorrencias = ocorrencias.filter(curso=curso)

    # Busca por ano
    ano = request.GET.get("ano")
    if ano:
        ocorrencias = ocorrencias.filter(ano=ano)

    context = {
        "ocorrencias": ocorrencias,
        "cursos": Ocorrencia.CURSOS,
        "anos": Ocorrencia.ANOS,
    }

    return render(request, "ocorrencias/listar.html", context)
    
    
