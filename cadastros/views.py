from .models import Material, Disciplina

from django.views.generic.edit import CreateView, UpdateView, DeleteView, ListView

from django.urls import reverse_lazy

class DisciplinaCreate(CreateView):
    model = Disciplina
    fields = ['nome']
    template_name = 'cadastros.form.html'
    success_url = reverse_lazy('index')  
    #pra qual pag vc vai mandar o usuario

class DisciplinaUpdate(UpdateView):
    model = Disciplina
    fields = ['nome']
    template_name = 'cadastros.form.html'
    success_url = reverse_lazy('index')  

class DisciplinaDelete(DeleteView):
    model = Disciplina
    fields = ['nome']
    template_name = 'cadastros.form.html'
    success_url = reverse_lazy('index')     

class DisciplinaList(ListView):
    model = Disciplina
    fields = ['nome']
    template_name = 'cadastros.form.html'
    success_url = reverse_lazy('index')     


