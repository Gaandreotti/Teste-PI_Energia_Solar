from django.contrib import admin
from .models import Cliente, Orcamento

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'email', 'telefone', 'cidade', 'criado_em')
    search_fields = ('nome', 'email')

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display  = ('cliente', 'consumo_kwh', 'custo_estimado', 'payback_anos', 'criado_em')

admin.site.site_header = "☀️ PI Energia Solar — Painel Admin"
admin.site.index_title = "Gerenciamento do Sistema"