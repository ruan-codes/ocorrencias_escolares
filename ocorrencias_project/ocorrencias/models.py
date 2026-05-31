from django.db import models


class Aluno(models.Model):
    class Curso(models.TextChoices):
        ADMINISTRACAO = "administracao", "Administração"
        ENFERMAGEM = "enfermagem", "Enfermagem"
        INFORMATICA = "informatica", "Informática"
        LOGISTICA = "logistica", "Logística"
        DS = "ds", "Desenvolvimento de Sistemas"

    ANOS = [(1, "1º Ano"), (2, "2º Ano"), (3, "3º Ano")]

    matricula = models.CharField(max_length=20, unique=True, db_index=True)
    nome = models.CharField(max_length=200, db_index=True)
    curso = models.CharField(max_length=50, choices=Curso.choices, db_index=True)
    ano = models.PositiveSmallIntegerField(choices=ANOS, db_index=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.matricula} — {self.nome}"

    @property
    def turma(self):
        return f"{self.get_curso_display()} {self.get_ano_display()}"

    class Meta:
        ordering = ["nome"]
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"


class Ocorrencia(models.Model):
    class Gravidade(models.TextChoices):
        LEVE = "leve", "Leve"
        MEDIA = "media", "Média"
        GRAVE = "grave", "Grave"

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.PROTECT,
        related_name="ocorrencias",
    )
    registrado_por = models.ForeignKey(
        "auth.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="ocorrencias_registradas",
    )
    data = models.DateField(db_index=True)
    descricao = models.TextField()
    gravidade = models.CharField(
        max_length=10,
        choices=Gravidade.choices,
        default=Gravidade.LEVE,
        db_index=True,
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.aluno.nome} — {self.get_gravidade_display()} — {self.data}"

    class Meta:
        ordering = ["-criado_em"]
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"
