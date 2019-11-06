from django import forms

from . models import Pessoa, Telefone

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome']
