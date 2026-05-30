from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("ocorrencias/", views.listar, name="listar"),
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("detalhe/<int:pk>/", views.detalhe, name="detalhe"),
    path("detalhe/<int:pk>/editar/", views.editar, name="editar"),
    path("detalhe/<int:pk>/excluir/", views.excluir, name="excluir"),

    # Gestão de alunos
    path("alunos/", views.listar_alunos, name="listar_alunos"),
    path("alunos/novo/", views.cadastrar_aluno, name="cadastrar_aluno"),
    path("alunos/<int:pk>/", views.detalhe_aluno, name="detalhe_aluno"),
    path("alunos/<int:pk>/editar/", views.editar_aluno, name="editar_aluno"),
]