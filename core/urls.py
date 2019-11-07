from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('lista', views.ListaContatosView.as_view(), name='lista'),
    path('cadastro', views.CadastrarContatoView.as_view(), name='cadastro_contato'),
    path('atualizar/<int:pk>', views.AtualizarContatoView.as_view(), name='atualizar_contato'),
    path('telefones/<int:pk>', views.ListaTelefonesView.as_view(), name='telefones'),
    path('telefones/<int:pk>/cadastro', views.CadastrarTelefoneView.as_view(), name='cadastro_telefone'),
    path('atualizar-telefone/<int:pk>', views.AtualizarTelefoneView.as_view(), name='atualizar_telefone'),
    path('deletar-contato/<int:pk>', views.DeletarContatoView.as_view(), name='deletar_contato'),
    path('deletar-telefone/<int:pk>', views.DeletarTelefoneView.as_view(), name='deletar_telefone'),
    path('', views.InicioView.as_view(), name='inicio')
]
