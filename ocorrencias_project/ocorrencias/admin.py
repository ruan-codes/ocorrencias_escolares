from django.contrib import admin
from .models import Ocorrencia

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ["nome_aluno", "curso", "ano", "gravidade", "data", "criado_em"]
    list_filter = ["curso", "ano", "gravidade"]
    search_fields = ["nome_aluno"]
    ordering = ["-criado_em"]
