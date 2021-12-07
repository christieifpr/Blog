from django.urls import path
from .views import DisciplinaCreate, DisciplinaUpdate

urlpatterns = [
    # Criar todos os endereços/rotas
    # path('endereço/', MinhaView.as_view(), name='referência/apelido'),

    path('cadastrar/disciplina/', DisciplinaCreate.as_view(), name='cadastrar-disciplina'),
    path('editar/disciplina/<int:pk>/', DisciplinaUpdate.as_view(), name='editar-disciplina'),

]
