from django.shortcuts import render, get_object_or_404
from django.http import Http404
from . models import Pessoa

class Handle404Mixin:
    template404 = None

    def get_context_error_404(self):
        raise NotImplemented('Método get_context_error_404 não implementado')

    def get_template_error_404(self):
        if self.template404 is None:
            raise NotImplemented('O atributo template404 não foi definido')
        return self.template404

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        
        except Http404:
            template = self.get_template_error_404()
            ctx = self.get_context_error_404()
            return render(request, template, context=ctx, status=404)

class GetPessoaMixin(Handle404Mixin):
    pessoa = None
    template404 = 'core/not_found.html'

    def get_pessoa(self):
        if self.pessoa is None:
            qs = Pessoa.objects.all()
            self.pessoa = get_object_or_404(qs, id=self.kwargs['pk'])
        return self.pessoa

    def get_context_error_404(self):
        return {
            'id': self.kwargs['pk'], 
            'msg': 'Contato não encontrado'
        }
