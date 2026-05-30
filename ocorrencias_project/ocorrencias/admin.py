from django.contrib import admin
from .models import Aluno, Ocorrencia


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display  = ["matricula", "nome", "curso", "ano", "ativo"]
    list_filter   = ["curso", "ano", "ativo"]
    search_fields = ["matricula", "nome"]
    ordering      = ["nome"]
    list_editable = ["ativo"]


@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display  = ["aluno", "curso_aluno", "ano_aluno", "gravidade", "data", "registrado_por", "criado_em"]
    list_filter   = ["gravidade", "aluno__curso", "aluno__ano"]
    search_fields = ["aluno__nome", "aluno__matricula", "descricao"]
    ordering      = ["-criado_em"]
    readonly_fields = ["registrado_por", "criado_em", "atualizado_em"]
    autocomplete_fields = ["aluno"]  # busca por nome/matrícula no campo aluno

    fieldsets = (
        ("Aluno", {
            "fields": ("aluno",)
        }),
        ("Ocorrência", {
            "fields": ("data", "gravidade", "descricao")
        }),
        ("Metadados", {
            "fields": ("registrado_por", "criado_em", "atualizado_em"),
            "classes": ("collapse",),
        }),
    )

    @admin.display(description="Curso", ordering="aluno__curso")
    def curso_aluno(self, obj):
        return obj.aluno.get_curso_display()

    @admin.display(description="Ano", ordering="aluno__ano")
    def ano_aluno(self, obj):
        return obj.aluno.get_ano_display()

    def save_model(self, request, obj, form, change):
        # Garante que o admin também preenche registrado_por
        if not obj.pk:
            obj.registrado_por = request.user
        super().save_model(request, obj, form, change)