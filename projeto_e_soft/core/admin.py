from django.contrib import admin
from core.models import Endereço

# Estrutura para ler os metadados contidos no BD com filtros para exibição do mesmo
class telaAdmin(admin.ModelAdmin):
    list_display = ('end', 'cep', 'cidade', 'uf')
    list_filter = ('end',)


admin.site.register(Endereço, telaAdmin)# Atrelando o model a classe para configurar a exibição
