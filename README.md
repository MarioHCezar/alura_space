# Requisitos:

- Python3.12;
- Django 5;
- venv
- pip install django
- pip freeze > requirements.txt

## Iniciar projeto Django:
- django-admin startproject setup .

## Carregar projeto:
- python3 manage.py runserver

## Esconder SECRET_KEY:
- importar os
- importar load_dotenv de dotenv
- criar arquivo .env com a SECRET_KEY
- em settings.py, substituir a variável SECRET_KEY por SECRET_KEY = os.getenv('SECRET_KEY')

## Criar app (template, semelhante a um componente):
- python3 manage.py startapp nome_do_app
- Obs.: necessário incluir o nome do app no array de INSTALLED_APPS (semelhante a um módulo no Angular)

## Criar view:
- acessar o arquivo views.py do app desejado e definir função para acessar resposta http.
- Ex.:
  
```
from django.http import HttpResponse
def index(request):
        return HttpResponse('utilizar tags html ou retornar resposta da requisição')
```

## Definir novo path em urlpatterns:
- adicionar novo path no array de urlpatterns. Necessário importar o método criado acima de nome_do_app.views

## Isolar urls:
- dentro do diretório do app, criar novo arquivo urls.py, importando o path de djsango.urls e o método de nome_do_app.views.
Ex.:
```
from django.urls import path
from galeria.views import index

urlpatterns = [
        path('', index)
]
```

## Usando método include em django.urls
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('galeria.urls')),
]
```
## Ajustando uso de templates:

- Ajustar arquivo settings.py para incluir o diretório dos templates:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/alura_space-front-end')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
- ajustar método index em nome_do_app views.py para tratar a requisição e incluir o arquivo do template:
```
from django.shortcuts import render

def index(request):
        return render(request, 'index.html')
```

## Carregando arquivos estáticos (estilos, etc)
- necessário definir no arquivo settings.py em qual diretório ficarão os arquivos.
- criar um diretório static dentro de setup para armazenar estilos e assets
- definir STATICFILES_DIRS e STATIC_ROOT:
```
STATIC_URL = 'static/'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'setup/static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
- rodar comando ```python manage.py collectstatic```
- dentro do template html, envolver os endereços dos arquivos de estilos e assets com a marcação ```{% static '' %}```
- Ex.: ```<link rel="stylesheet" href="{% static '/styles/style.css' %}">```

## Renderizando outras páginas:
- para renderizar outras páginas, deve ser criada uma nova função para cada template que será exibido.
- Ex.:
```
from django.shortcuts import render

def index(request):
        return render(request, 'galeria/index.html')

def imagem(request):
        return render(request, 'galeria/imagem.html') 
```
- após isso, deve ser criada a rota (path) no urlpatterns do arquivo urls.py da view desejada.
- Ex.:
```
from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
        path('', index),
        path('imagem/', imagem)
]
```
- é uma boa prática atribuir um name ao path:
```
urlpatterns = [
        path('', index, name='index'),
        path('imagem/', imagem, name='imagem'),
]
```
- com isso, a vinculução no template fica mais simples e legível:
```<a href="{% url 'index' %}">```
continua...
