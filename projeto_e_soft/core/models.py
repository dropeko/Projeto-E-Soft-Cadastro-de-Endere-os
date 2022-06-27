from django.db import models


# Aqui faz a abstração dos objetos de Banco de DADOS / Transforma todas as TABELAS em CLASSES
class Endereço(models.Model):#Criando uma classe representando uma tabela para manipular a BD
    end = models.CharField(max_length=200, verbose_name='ENDEREÇO')
    cep = models.CharField(max_length=200, verbose_name='CEP')
    num = models.IntegerField(verbose_name='NÚMERO')
    bairro = models.CharField(max_length=100, verbose_name='BAIRRO')
    cidade = models.CharField(max_length=100, verbose_name='CIDADE')
    uf = models.CharField(max_length=30, verbose_name='UNIDADE FEDERATIVA')
    descrição = models.TextField(blank=True, null=True)#Parametro para aceitar valores em branco e nulos

    class Meta():
        db_table = 'ENDEREÇOS'

    def __str__(self):
        return self.end



