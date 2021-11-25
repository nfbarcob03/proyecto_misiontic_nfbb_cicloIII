from authApp.models.inmueble import Inmueble
from authApp.models.tipoInmueble import TipoInmueble
from rest_framework import serializers
from authApp.models.user import User

##from authApp.serializers.userSerializer import UserSerializer
from authApp.serializers.tipoInmuebleSerializer import TipoInmuebleSerializer

class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields = ['id', 'id_arrendatario', 'precio', 'habitaciones', 'tipo', 'disponible', 'fechaCreacion']

        
    def to_representation(self, obj):
        inmueble = Inmueble.objects.get(id=obj.id)
        tipoInmueble = TipoInmueble.objects.get(id=obj.tipo.id)
        arrendatario = User.objects.get(id=obj.id_arrendatario.id)
##           arrendatarioSerializer = UserSerializer(data=arrendatario)
        return {
            'id': inmueble.id,
            'id_arrendatario':inmueble.id_arrendatario.id,
            'nombre_arrenatario': arrendatario.name,
            'precio': inmueble.precio,
            'habitaciones': inmueble.habitaciones,
            'id_tipo': tipoInmueble.id,
            'tipo': tipoInmueble.nombre,
            'disponible': inmueble.disponible,
            'fechaCreacion': inmueble.fechaCreacion,
        }
    
    