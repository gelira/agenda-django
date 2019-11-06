from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('lista', views.ListaContatosView.as_view(), name='lista'),
    path('cadastro', views.CadastrarContatoView.as_view(), name='cadastro_contato'),
    path('telefones/<int:pk>', views.ListaTelefonesView.as_view(), name='telefones'),
]
