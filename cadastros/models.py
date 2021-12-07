from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
#nome e nome -- exibição p o admin

class Material(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    link = models.CharField(max_length=100, blank=True, null=True)
    arquivo = models.FileField()
    data = models.DateTimeField(auto_now_add=True)
    disciplina = models.ForeignKey(Disciplina, on_delete= models.PROTECT)

    def __str__(self):
        return "{}/{}".format(self.descricao, self.disciplina)