from django.db import models
# Create your models here.

class Articulo(models.Model):

    nombre=models.CharField(max_length=50)
    stock=models.IntegerField()
    precio=models.IntegerField()
    
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

