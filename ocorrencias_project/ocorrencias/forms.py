from django import forms
from .models import Ocorrencia

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ["nome_aluno", "curso", "ano", "data", "descricao", "gravidade"]
        widgets = {
            "nome_aluno": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nome completo do aluno"
            }),
            "curso": forms.Select(attrs={"class": "form-select"}),
            "ano": forms.Select(attrs={"class": "form-select"}),
            "gravidade": forms.Select(attrs={"class": "form-select"}),
            "data": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
            "descricao": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Descreva detalhadamente o ocorrido..."
            }),
        }

        labels = {
            "nome_aluno": "Nome do Aluno",
            "curso": "Curso",
            "ano": "Ano",
            "data": "Data da Ocorrência",
            "descricao": "Descrição",
            "gravidade": "Gravidade",
        }

    def clean_nome_aluno(self):
        nome = self.cleaned_data.get("nome_aluno", "")
        if not nome or not nome.strip:
            raise forms.ValidationError("O nome do aluno não pode estar em branco.")
        return nome.strip()      