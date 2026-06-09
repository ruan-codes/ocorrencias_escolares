from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, Q
from ocorrencias.models import Aluno, Ocorrencia
from ocorrencias.forms import AlunoForm, OcorrenciaForm


# ──────────────────────────────────────────────
# DASHBOARD
# ──────────────────────────────────────────────

@login_required
def dashboard(request):
    stats = Ocorrencia.objects.aggregate(
        total=Count("id"),
        leves=Count("id", filter=Q(gravidade="leve")),
        medias=Count("id", filter=Q(gravidade="media")),
        graves=Count("id", filter=Q(gravidade="grave")),
    )

    cursos_qs = (
        Ocorrencia.objects
        .values("aluno__curso")
        .annotate(quantidade=Count("id"))
        .order_by("-quantidade")
    )
    cursos_dict = {item["aluno__curso"]: item["quantidade"] for item in cursos_qs}

    cursos_data = [
        {"curso": label, "quantidade": cursos_dict.get(valor, 0)}
        for valor, label in Aluno.Curso.choices
    ]

    context = {
        "total":        stats["total"],
        "leves":        stats["leves"],
        "medias":       stats["medias"],
        "graves":       stats["graves"],
        "recentes":     Ocorrencia.objects.select_related("aluno").all()[:5],
        "cursos_data":  cursos_data,
        "total_alunos": Aluno.objects.filter(ativo=True).count(),
    }
    return render(request, "ocorrencias/dashboard.html", context)


# ──────────────────────────────────────────────
# OCORRÊNCIAS
# ──────────────────────────────────────────────

@login_required
def listar(request):
    ocorrencias = Ocorrencia.objects.select_related("aluno", "registrado_por")

    nome = request.GET.get("nome", "").strip()
    if nome:
        ocorrencias = ocorrencias.filter(aluno__nome__icontains=nome)

    curso = request.GET.get("curso", "")
    if curso:
        ocorrencias = ocorrencias.filter(aluno__curso=curso)

    ano = request.GET.get("ano", "")
    if ano:
        ocorrencias = ocorrencias.filter(aluno__ano=ano)

    gravidade = request.GET.get("gravidade", "")
    if gravidade:
        ocorrencias = ocorrencias.filter(gravidade=gravidade)

    paginator = Paginator(ocorrencias, 20)
    page = paginator.get_page(request.GET.get("page"))

    context = {
        "ocorrencias": page,
        "page_obj":    page,
        "cursos":      Aluno.Curso.choices,
        "anos":        [(str(v), l) for v, l in Aluno.ANOS],
        "gravidades":  Ocorrencia.Gravidade.choices,
    }
    return render(request, "ocorrencias/listar.html", context)


@login_required
def cadastrar(request):
    aluno_pk = request.GET.get("aluno")
    initial = {"aluno": aluno_pk} if aluno_pk else {}

    form = OcorrenciaForm(request.POST or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        ocorrencia = form.save(commit=False)
        ocorrencia.registrado_por = request.user
        ocorrencia.save()
        messages.success(request, "Ocorrência cadastrada com sucesso!")
        return redirect("listar")
    return render(request, "ocorrencias/cadastrar.html", {"form": form})


@login_required
def detalhe(request, pk):
    ocorrencia = get_object_or_404(
        Ocorrencia.objects.select_related("aluno", "registrado_por"), pk=pk
    )
    return render(request, "ocorrencias/detalhe.html", {"ocorrencia": ocorrencia})


@login_required
def editar(request, pk):
    ocorrencia = get_object_or_404(Ocorrencia, pk=pk)
    form = OcorrenciaForm(request.POST or None, instance=ocorrencia)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Ocorrência atualizada com sucesso!")
        return redirect("detalhe", pk=pk)
    return render(request, "ocorrencias/editar.html", {
        "form":       form,
        "ocorrencia": ocorrencia,
    })


@login_required
def excluir(request, pk):
    ocorrencia = get_object_or_404(Ocorrencia, pk=pk)
    if request.method == "POST":
        ocorrencia.delete()
        messages.success(request, "Ocorrência excluída com sucesso!")
        return redirect("listar")
    return render(request, "ocorrencias/excluir.html", {"ocorrencia": ocorrencia})


# ──────────────────────────────────────────────
# ALUNOS
# ──────────────────────────────────────────────

@login_required
def listar_alunos(request):
    alunos = Aluno.objects.filter(ativo=True).annotate(
        total_ocorrencias=Count("ocorrencias")
    )

    nome = request.GET.get("nome", "").strip()
    if nome:
        alunos = alunos.filter(nome__icontains=nome)

    curso = request.GET.get("curso", "")
    if curso:
        alunos = alunos.filter(curso=curso)

    ano = request.GET.get("ano", "")
    if ano:
        alunos = alunos.filter(ano=ano)

    paginator = Paginator(alunos, 20)
    page = paginator.get_page(request.GET.get("page"))

    context = {
        "alunos":   page,
        "page_obj": page,
        "cursos":   Aluno.Curso.choices,
        "anos":     [(str(v), l) for v, l in Aluno.ANOS],
    }
    return render(request, "ocorrencias/listar_alunos.html", context)


@login_required
def cadastrar_aluno(request):
    form = AlunoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Aluno cadastrado com sucesso!")
        return redirect("listar_alunos")
    return render(request, "ocorrencias/cadastrar_aluno.html", {"form": form})


@login_required
def detalhe_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    ocorrencias_qs = aluno.ocorrencias.select_related("registrado_por").order_by("-data")

    # Calcula stats sobre o total antes de paginar
    stats = ocorrencias_qs.aggregate(
        total=Count("id"),
        leves=Count("id", filter=Q(gravidade="leve")),
        medias=Count("id", filter=Q(gravidade="media")),
        graves=Count("id", filter=Q(gravidade="grave")),
    )

    paginator = Paginator(ocorrencias_qs, 10)
    page = paginator.get_page(request.GET.get("page"))

    context = {
        "aluno":       aluno,
        "ocorrencias": page,
        "page_obj":    page,
        "stats":       stats,
    }
    return render(request, "ocorrencias/detalhe_aluno.html", context)


@login_required
def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Dados do aluno atualizados com sucesso!")
        return redirect("detalhe_aluno", pk=pk)
    return render(request, "ocorrencias/editar_aluno.html", {
        "form":  form,
        "aluno": aluno,
    })