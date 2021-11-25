from django.db import models
from .user import User


class TipoInmueble(models.Model):
    id= models.BigAutoField('id_tipo', primary_key=True)
    nombre = models.CharField('Tipo', max_length = 30)