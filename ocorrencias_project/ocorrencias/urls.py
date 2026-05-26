from django.urls import path
import views

urlpatterns = [
    path("", views.listar, name="listar"),
    path("cadastrar/", views.cadastrar, name="cadastrar")
]