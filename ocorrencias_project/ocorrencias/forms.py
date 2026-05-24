from django import forms
from models import Ocorrencia

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ["nome_aluno", "curso", "ano", "data", "descricao", "gravidade"]
        widgets = {
            'nome_aluno': forms.TextInput(attrs={
                'placeholder': 'Nome completo do aluno'
            }),
            'data': forms.DateInput(attrs={
                'type': 'date'
            }),
            'descricao': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Descreva detalhadamente o ocorrido...'
            }),
        }

        labels = {
            'nome_aluno': 'Nome do Aluno',
            'curso': 'Curso',
            'ano': 'Ano',
            'data': 'Data da Ocorrência',
            'descricao': 'Descrição',
            'gravidade': 'Gravidade',
        }

        def clean_nome_aluno(self):
            nome = self.cleaned_data.get("nome_aluno")
            if not nome or not nome.strip:
                raise forms.ValidationError("O nome do aluno não pode estar em branco.")
            return nome.strip()