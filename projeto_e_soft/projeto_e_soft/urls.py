
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('evento/', views.lista_cadastro), #Rota criada para acessar a view de exibição da pagina principal com o template html criado
    path('', RedirectView.as_view(url='/evento/')),#Rota criada para redirecionar a pagina principal para a da lista de cadastro
    path('evento/cadastro/', views.cadastro), #Rota criada para redirecionar o user a pagina de cadastro de novo endereço
    path('evento/cadastro/submit', views.submit_cadastro) #Rota criada para redirecionar o user a pagina submit de novo cadastro

]
