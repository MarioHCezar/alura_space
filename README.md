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
