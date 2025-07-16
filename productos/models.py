from django.db import models
from django.utils import timezone
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # cascade its behavior is to delete all products in this category if the category is deleted
    # protect its behavior is to prevent deletion of the category if there are products in it
    # restrict its behavior is to prevent deletion of the category if there are products in it
    # set_null its behavior is to set the category to null if the category is deleted
    # set_default its behavior is to set the category to a default value if the category is deleted
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
