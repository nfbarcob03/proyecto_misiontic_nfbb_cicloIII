from django.db import models
from .user import User
from .inmueble import Inmueble

class Inmueble_arrendado(models.Model):
    id= models.BigAutoField(primary_key=True)
    id_inmueble= models.ForeignKey(Inmueble, related_name='id_inmueble', on_delete=models.CASCADE)
    id_arrendador= models.ForeignKey(User, related_name='id_user_inmueble_arrendado', on_delete=models.CASCADE)
    fecha_inicio= models.DateField()
    fecha_fin=models.DateField()