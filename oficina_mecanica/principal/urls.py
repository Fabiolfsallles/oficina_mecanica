from django.urls import path
from . import views

urlpatterns = [
    # URLs para Clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/cadastro/', views.cadastro_cliente, name='cadastro_cliente'),

    # URLs para Produtos
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/cadastro/', views.cadastro_produto, name='cadastro_produto'),

    # URLs para Ordens de Serviço
    path('ordens-servico/', views.lista_ordens_servico, name='lista_ordens_servico'),
    path('ordens-servico/gerar/', views.gerar_ordem_servico, name='gerar_ordem_servico'),

    # URLs para Agendamentos
    path('agendamentos/', views.lista_agendamentos, name='lista_agendamentos'),
    path('agendamentos/novo/', views.novo_agendamento, name='novo_agendamento'),
]