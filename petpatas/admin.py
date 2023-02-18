from django.contrib import admin

from petpatas.models import Servicos

class ListandoServicos(admin.ModelAdmin):
    list_display = ("nome", "descricao", "ativo")
    list_display_links = ("nome", "descricao")
    list_editable = ("ativo",)
    search_fields = ("nome",)

admin.site.register(Servicos, ListandoServicos)
