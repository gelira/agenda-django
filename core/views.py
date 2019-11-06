from django.views.generic import ListView

from . models import Pessoa

class ListaContatosView(ListView):
    model = Pessoa
    template_name = 'core/lista_contatos.html'
    context_object_name = 'pessoas'
