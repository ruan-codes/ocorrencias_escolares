from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("ocorrencias/", views.listar, name="listar"),
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("detalhe/<int:pk>/", views.detalhe, name="detalhe"),
    path("detalhe/<int:pk>/editar/", views.editar, name="editar"),
    path("detalhe/<int:pk>/excluir/", views.excluir, name="excluir"),
]