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

.
.
. 

continua...
