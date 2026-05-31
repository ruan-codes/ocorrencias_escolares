from django import forms
from .models import Aluno, Ocorrencia


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["matricula", "nome", "curso", "ano"]
        widgets = {
            "matricula": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex: 2024001",
            }),
            "nome": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nome completo do aluno",
            }),
            "curso": forms.Select(attrs={"class": "form-select"}),
            "ano": forms.Select(attrs={"class": "form-select"}),
        }
        labels = {
            "matricula": "Matrícula",
            "nome": "Nome do aluno",
            "curso": "Curso",
            "ano": "Ano",
        }

    def clean_nome(self):
        nome = self.cleaned_data.get("nome", "")
        if not nome.strip():
            raise forms.ValidationError("O nome do aluno não pode estar em branco.")
        return nome.strip()

    def clean_matricula(self):
        matricula = self.cleaned_data.get("matricula", "").strip()
        if not matricula:
            raise forms.ValidationError("A matrícula não pode estar em branco.")
        return matricula


class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ["aluno", "data", "descricao", "gravidade"]
        widgets = {
            "aluno": forms.Select(attrs={"class": "form-select"}),
            "gravidade": forms.Select(attrs={"class": "form-select"}),
            "data": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),
            "descricao": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Descreva detalhadamente o ocorrido...",
            }),
        }
        labels = {
            "aluno": "Aluno",
            "data": "Data da ocorrência",
            "descricao": "Descrição",
            "gravidade": "Gravidade",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["aluno"].queryset = Aluno.objects.filter(ativo=True).order_by("nome")
