from django.urls import path
from .views import DisciplinaCreate, DisciplinaUpdate, MaterialCreate, MaterialUpdate, MaterialList, MaterialDelete

urlpatterns = [
    # Criar todos os endereços/rotas
    # path('endereço/', MinhaView.as_view(), name='referência/apelido'),

    path('cadastrar/disciplina/', DisciplinaCreate.as_view(), name='cadastrar-disciplina'),
    path('editar/disciplina/<int:pk>/', DisciplinaUpdate.as_view(), name='editar-disciplina'),


#mexi aq oito do dois
    path('cadastrar/material/', MaterialCreate.as_view(), name='cadastrar-material'),
    path('editar/material/<int:pk>/', MaterialUpdate.as_view(), name='editar-material'),


]
