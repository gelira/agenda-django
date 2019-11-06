from django import forms

from . models import Pessoa, Telefone

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome']

class TelefoneForm(forms.ModelForm):
    pessoa = forms.ModelChoiceField(
        queryset=Pessoa.objects.all(),
        disabled=True,
        widget=forms.HiddenInput
    )
    class Meta:
        model = Telefone
        fields = ['pessoa', 'numero']
