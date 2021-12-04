from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

def __str__(self):
    return self.nome + - + self.nome
#nome e nome -- exibição p o admin

class Material(models.Model):
    material = models.CharField(max_length=100)
    disciplina = models.ForeignKey(Disciplina, on_delete= models.PROTECT)

def __str__(self):
    return self.material + - + self.disciplina