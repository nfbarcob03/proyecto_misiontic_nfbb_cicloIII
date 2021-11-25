from authApp.models.tipoInmueble import TipoInmueble
from rest_framework import serializers

class TipoInmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInmueble
        fields = ['id', 'nombre']
