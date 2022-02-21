from django.db import models
from django.conf import settings

class Categoria(models.Model):
    nome = models.CharField(blank=False, max_length=120)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(blank=False, max_length=120)
    autor = models.CharField(blank=False, max_length=120)
    nr_paginas = models.IntegerField(blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Catalogo(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    livros = models.ManyToManyField(Livro)
