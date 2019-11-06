from django.shortcuts import reverse
from django.views.generic import ListView, CreateView

from . models import Pessoa, Telefone
from . forms import PessoaForm, TelefoneForm

class ListaContatosView(ListView):
    model = Pessoa
    template_name = 'core/lista_contatos.html'
    context_object_name = 'pessoas'

class ListaTelefonesView(ListView):
    template_name = 'core/lista_telefones.html'
    context_object_name = 'telefones'
    pessoa = None

    def get_queryset(self):
        self.pessoa = Pessoa.objects.get(id=self.kwargs['pk'])
        return self.pessoa.telefones.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['pessoa'] = self.pessoa
        return ctx

class CadastrarContatoView(CreateView):
    form_class = PessoaForm
    template_name = 'core/form_contato.html'

    def get_success_url(self):
        return reverse('core:lista')

class CadastrarTelefoneView(CreateView):
    template_name = 'core/form_telefones.html'
    form_class = TelefoneForm
    pessoa = None

    def get_pessoa(self):
        return Pessoa.objects.get(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['pessoa'] = self.get_pessoa()
        return ctx

    def get_initial(self):
        initial = super().get_initial()
        initial['pessoa'] = self.kwargs['pk']
        return initial

    def get_success_url(self):
        return reverse('core:telefones', kwargs={'pk': self.kwargs['pk']})
