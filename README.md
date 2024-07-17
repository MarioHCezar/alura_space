# Utilizacao do Django ORM

- A utilizacao do Django ORM simplifica o processo de manipulacao do banco de dados, substituindo as queries e insercoes/alteracoes por metodos de uma clase
- Ex.:
Isso:
```
class Person(models.Model):
    first_name = models.CharField(max_length=30)
```
Equivale a isso:
```
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
```
- Essa configuração do ORM é feita no arquivo models.py utilizando as classes do Python.
Ex.:
```
from django.db import models

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
```
