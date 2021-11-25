from django.db import models
from .user import User
from .tipoInmueble import TipoInmueble


class Inmueble(models.Model):
    id= models.BigAutoField('id_inmueble', primary_key=True)
    id_arrendatario = models.ForeignKey(User, related_name='id_user_inmueble_arrendatario', on_delete=models.CASCADE)
    precio= models.IntegerField(blank=False)
    habitaciones= models.IntegerField(blank=False)
    tipo= models.ForeignKey(TipoInmueble, related_name='id_inmueble_tipoinmueble', on_delete=models.CASCADE)
    disponible= models.BooleanField(default=False)
    fechaCreacion= models.DateField()