from .models import Disciplina, Material

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

class DisciplinaCreate(CreateView):
    model = Disciplina
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')  
    #pra qual pag vc vai mandar o usuario

class DisciplinaUpdate(UpdateView):
    model = Disciplina
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')  

class DisciplinaDelete(DeleteView):
    model = Disciplina
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')     

class DisciplinaList(ListView):
    model = Disciplina
    template_name = 'cadastros/form.html'



class MaterialCreate(CreateView):
    model = Material
    fields = ['nome do material']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')  
    #pra qual pag vc vai mandar o usuario


class MaterialUpdate(UpdateView):
    model = Material
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')  

class MaterialDelete(DeleteView):
    model = Material
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')     

class MaterialList(ListView):
    model = Material
    template_name = 'cadastros/form.html'