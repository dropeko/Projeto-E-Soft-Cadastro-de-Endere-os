from django.shortcuts import render, redirect
from core.models import Endereço

# Funções para renderizar os templates HTMLs criados para as paginas do sistema
def lista_cadastro(request):
    end = Endereço.objects.all() #Comando para gerar uma lista da BD
    dados = {'enderecos': end} #Criando uma chave via dicionário para identificar a response no template HTML
    return render(request, 'enderecos.html', dados) #Retornando a request, direcionando para o arquivo do template com o parametro de dados passado


def cadastro(request):# Função para renderizar a pagina HTML de cadastro quando chamada
    return render(request, 'cadastro.html')


def submit_cadastro(request):# Função para extrair os dados da página HTML de cadastro e cria-las no model do BD
    if request.POST:
        end = request.POST.get('end')
        cep = request.POST.get('cep')
        num = request.POST.get('num')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        uf = request.POST.get('uf')
        descricao = request.POST.get('descriçao')
        Endereço.objects.create(end = end,
                                cep = cep,
                                num = num,
                                bairro = bairro,
                                cidade = cidade,
                                uf = uf,
                                descrição = descricao)
    return redirect('/')


