from django.db import models


class Usuario(models.Model):
    # id usuario
    id_usuario = models.AutoField(primary_key=True)

    # nome textfield
    nome = models.TextField(max_length=255)

    # idade integerfield
    idade = models.IntegerField()