from authApp.models.inmueble_arrendado import Inmueble_arrendado
from rest_framework import serializers

class InmuebleArrendadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble_arrendado
        fields = ['id', 'id_inmueble','id_arrendador','fecha_inicio','fecha_fin']