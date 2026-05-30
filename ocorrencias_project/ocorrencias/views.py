from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# pyrefly: ignore [missing-import]
from .models import Ocorrencia
# pyrefly: ignore [missing-import]
from .forms import OcorrenciaForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q

def dashboard(request):
    stats = Ocorrencia.objects.aggregate(
        total = Count("id"),
        leves = Count("id", filter=Q(gravidade="leve")),
        medias = Count("id", filter=Q(gravidade="media")),
        graves = Count("id", filter=Q(gravidade="grave")),
    )

    cursos_qs = (
        Ocorrencia.objects
        .values("curso")
        .annotate(quantidade=Count("id"))
        .order_by("-quantidade")
    )
    cursos_dict = {item["curso"]: item["quantidade"] for item in cursos_qs}
    
    cursos_data = [
        {"curso": label, "quantidade": cursos_dict.get(valor, 0)}
        for valor, label in Ocorrencia.CURSOS
    ]

    context = {
        "total": stats["total"],
        "leves": stats["leves"],
        "medias": stats["medias"],
        "graves": stats["graves"],
        "recentes": Ocorrencia.objects.all()[:5],
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
        
    
    
