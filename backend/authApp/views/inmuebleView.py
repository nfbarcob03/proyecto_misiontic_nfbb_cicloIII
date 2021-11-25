from django.conf import settings
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from datetime import date

from authApp.models.inmueble import Inmueble
from authApp.serializers.inmuebleSerializer import InmuebleSerializer

class InmuebleView(views.APIView):
  
    def delete(self, request, *args, **kwargs):
        queryset = Inmueble.objects.all()
        serializer_class = InmuebleSerializer
        permission_classes = (IsAuthenticated,)

        inmueble= Inmueble.objects.filter(id=kwargs['pk']).first()
        inmueble.delete()
        stringResponse = {'detail':'Registro liminado'}
        return Response(stringResponse)

    def post(self, request, *args, **kwargs):
        id_user_body = request.data.get("id_arrendatario")
        
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != id_user_body:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        request.data["fechaCreacion"] = date.today()
        serializer = InmuebleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        stringResponse = {'detail':'Excelente'}
    
        return Response(serializer.data,status=status.HTTP_201_CREATED)


    def put(self, request, *args, **kwargs):

        permission_classes = (IsAuthenticated,)

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        inmueble= Inmueble.objects.filter(id=int(kwargs['pk'])).first()

        if valid_data['user_id'] != request.data['id_arrendatario']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        request.data["fechaCreacion"] = date.today()
        serializer = InmuebleSerializer(inmueble, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        
    def get(self, request, *args, **kwargs):
        
        inmueble= Inmueble.objects.filter(id=kwargs['pk']).first()
        serializer = InmuebleSerializer(inmueble)
        return Response(serializer.data)

    
class AllInmuebles(generics.ListAPIView):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer
    
  ##  def get_queryset(self):
  ##      queryset = self.model.objects.all()
  ##      return queryset
    
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = InmuebleSerializer(queryset, many=True)
        ##respuesta = [InmuebleSerializer(inmueble).data for inmueble in queryset ]
        return Response(serializer.data)