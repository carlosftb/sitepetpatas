from django.contrib import admin

from petpatas.models import Servicos

class ListandoServicos(admin.ModelAdmin):
    list_display = ("nome_servico", "descricao", "ativo")
    list_display_links = ("nome_servico", "descricao")
    list_editable = ("ativo",)
    search_fields = ("nome_servico",)

admin.site.register(Servicos, ListandoServicos)
