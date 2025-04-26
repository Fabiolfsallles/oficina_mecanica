from django.contrib import admin
from .models import Cliente, Produto, OrdemDeServico, Agendamento

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(OrdemDeServico)
admin.site.register(Agendamento)