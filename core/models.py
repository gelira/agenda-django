from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    pessoa = models.ForeignKey(
        to=Pessoa,
        on_delete=models.CASCADE,
        related_name='telefones'
    )

    def __str__(self):
        return self.numero
