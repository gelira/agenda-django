from django.views.generic import ListView

from . models import Pessoa, Telefone

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
