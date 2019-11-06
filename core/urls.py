from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('lista', views.ListaContatosView.as_view(), name='lista')
]
