from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'profissao',
                     'data_criacao', 'categoria',)
    list_display_links = ('id', 'nome', 'sobrenome',)
    list_filter = ('profissao', 'data_criacao', 'categoria',)
    list_editable = ('profissao',)
    search_fields = ('nome', 'sobrenome', 'profissao',)
    list_per_page = 5



admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)


