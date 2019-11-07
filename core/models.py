from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

class TimestampedModel(SafeDeleteModel):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Pessoa(TimestampedModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'pessoas'
        ordering = ['nome', '-created']

class Telefone(TimestampedModel):
    numero = models.CharField(max_length=20)
    pessoa = models.ForeignKey(
        to=Pessoa,
        on_delete=models.CASCADE,
        related_name='telefones'
    )

    def __str__(self):
        return self.numero

    class Meta:
        db_table = 'telefones'
        ordering = ['numero', '-created']
