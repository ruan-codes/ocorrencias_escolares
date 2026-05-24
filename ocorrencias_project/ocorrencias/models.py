from django.db import models

class Ocorrencia(models.Model):
    CURSOS = [
        ('administracao', 'Administração'),
        ('enfermagem', 'Enfermagem'),
        ('informatica', 'Informática'),
        ('logistica', 'Logística'),
        ('ds', 'Desenvolvimento de Sistemas'),
    ]

    ANOS = [
        ('1', '1º Ano'),
        ('2', '2º Ano'),
        ('3', '3º Ano'),
    ]

    GRAVIDADES = [
        ('leve', 'Leve'),
        ('media', 'Média'),
        ('grave', 'Grave'),
    ]

    nome_aluno = models.CharField(max_length=200)
    curso = models.CharField(max_length=50, choices=CURSOS)
    ano = models.CharField(max_length=1, choices=ANOS)
    data = models.DateField()
    descricao = models.TextField()
    gravidade = models.CharField(max_length=10, choices=GRAVIDADES)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome_aluno} - {self.get_curso_display()} {self.get_ano_display()}'

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'