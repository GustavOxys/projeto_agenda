from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30, blank=True) 
    email = models.CharField(max_length=30, blank=True)
    profissao = models.CharField(max_length=30)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(max_length=50, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome
