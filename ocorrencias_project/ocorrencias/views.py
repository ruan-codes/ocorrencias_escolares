from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Ocorrencia
from .forms import OcorrenciaForm
from django.contrib.auth.decorators import login_required

def dashboard(request):
    total = Ocorrencia.objects.count()
    leves = Ocorrencia.objects.filter(gravidade="leve").count()
    medias = Ocorrencia.objects.filter(gravidade="media").count()
    graves = Ocorrencia.objects.filter(gravidade="grave").count()
    recentes = Ocorrencia.objects.all()[:5]
    
    cursos_data = []
    for valor, label in Ocorrencia.CURSOS:
        quantidade = Ocorrencia.objects.filter(curso=valor).count()
        cursos_data.append({"curso": label, "quantidade": quantidade})
        
    context = {
        "total": total,
        "leves": leves,
        "medias": medias,
        "graves": graves,
        "recentes": recentes,
        "cursos_data": cursos_data,
    }
    
    return render(request, "ocorrencias/dashboard.html", context)
    
    
@login_required
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

def detalhe(request, pk):
    ocorrencia = get_object_or_404(Ocorrencia, pk=pk)
    return render(request, "ocorrencias/detalhe.html", {"ocorrencia": ocorrencia})

@login_required
def editar(request, pk):
    ocorrencia = get_object_or_404(Ocorrencia, pk=pk)
    if request.method == "POST":
        form = OcorrenciaForm(request.POST, instance=ocorrencia)
        if form.is_valid():
            form.save()
            messages.success(request, "Ocorrência atualizada com sucesso!")
            return redirect("detalhe", pk=pk)
    else:
        form = OcorrenciaForm(instance=ocorrencia)
    
    return render(request, "ocorrencias/editar.html", {"form": form, "ocorrencia": ocorrencia})

@login_required
def excluir(request, pk):
    ocorrencia = get_object_or_404(Ocorrencia, pk=pk)
    if request.method == "POST":
        ocorrencia.delete()
        messages.success(request, "Ocorrência excluída com sucesso!")
        return redirect("listar")
    
    return render(request, "ocorrencias/excluir.html", {"ocorrencia": ocorrencia})
        
    
    
