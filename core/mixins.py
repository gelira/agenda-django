from . models import Pessoa

class GetPessoaMixin:
    pessoa = None

    def get_pessoa(self):
        if self.pessoa is None:
            self.pessoa = Pessoa.objects.get(id=self.kwargs['pk'])
        return self.pessoa
