from django.urls import reverse, reverse_lazy
from django.views import generic

from . models import Pessoa, Telefone
from . forms import PessoaForm, TelefoneForm
from . mixins import GetPessoaMixin, Handle404Mixin

class InicioView(generic.TemplateView):
    template_name = 'core/inicio.html'

class ListaContatosView(generic.ListView):
    model = Pessoa
    template_name = 'core/lista_contatos.html'
    context_object_name = 'pessoas'

class ListaTelefonesView(GetPessoaMixin, generic.ListView):
    template_name = 'core/lista_telefones.html'
    context_object_name = 'telefones'

    def get_queryset(self):
        return self.get_pessoa().telefones.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['pessoa'] = self.pessoa
        return ctx

class CadastrarContatoView(generic.CreateView):
    form_class = PessoaForm
    template_name = 'core/form_contato.html'
    success_url = reverse_lazy('core:lista')

class CadastrarTelefoneView(GetPessoaMixin, generic.CreateView):
    template_name = 'core/form_telefones.html'
    form_class = TelefoneForm

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

class AtualizarContatoView(Handle404Mixin, generic.UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'core/atualizar_contato.html'
    context_object_name = 'pessoa'
    template404 = 'core/not_found.html'
    
    def get_success_url(self):
        return reverse('core:telefones', kwargs={'pk': self.object.id})

    def get_context_error_404(self):
        return {
            'id': self.kwargs['pk'], 
            'msg': 'Contato não encontrado'
        }

class AtualizarTelefoneView(Handle404Mixin, generic.UpdateView):
    model = Telefone
    form_class = TelefoneForm
    template_name = 'core/atualizar_telefone.html'
    context_object_name = 'telefone'
    template404 = 'core/not_found.html'

    def get_success_url(self):
        return reverse('core:telefones', kwargs={'pk': self.object.pessoa_id})

    def get_context_error_404(self):
        return {
            'id': self.kwargs['pk'], 
            'msg': 'Telefone não encontrado'
        }

class DeletarContatoView(Handle404Mixin, generic.DeleteView):
    model = Pessoa
    template_name = 'core/deletar_contato.html'
    context_object_name = 'pessoa'
    success_url = reverse_lazy('core:lista')
    template404 = 'core/not_found.html'

    def get_context_error_404(self):
        return {
            'id': self.kwargs['pk'], 
            'msg': 'Contato não encontrado'
        }

class DeletarTelefoneView(Handle404Mixin, generic.DeleteView):
    model = Telefone
    template_name = 'core/deletar_telefone.html'
    context_object_name = 'telefone'
    template404 = 'core/not_found.html'

    def get_success_url(self):
        return reverse('core:telefones', kwargs={'pk': self.object.pessoa_id})

    def get_context_error_404(self):
        return {
            'id': self.kwargs['pk'], 
            'msg': 'Telefone não encontrado'
        }
