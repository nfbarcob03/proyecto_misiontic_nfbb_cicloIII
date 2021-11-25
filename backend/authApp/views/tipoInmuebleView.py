from django.conf import settings
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.tipoInmueble import TipoInmueble
from authApp.serializers.tipoInmuebleSerializer import TipoInmuebleSerializer

class TipoInmuebleView(views.APIView):
  
    def delete(self, request, *args, **kwargs):
        queryset = TipoInmueble.objects.all()
        serializer_class = TipoInmuebleSerializer
        permission_classes = (IsAuthenticated,)

        tipoInmueble= TipoInmueble.objects.filter(id=kwargs['pk']).first()
        tipoInmueble.delete()
        stringResponse = {'detail':'Registro liminado'}
        return Response(stringResponse)

    def post(self, request, *args, **kwargs):
        id_user_body = request.data.pop("id_user")
        
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != id_user_body:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = TipoInmuebleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        stringResponse = {'detail':'Excelente'}
    
        return Response(serializer.data,status=status.HTTP_201_CREATED)


    def put(self, request, *args, **kwargs):

        permission_classes = (IsAuthenticated,)

        id_user_body = request.data.pop("id_user")
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != id_user_body:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        tipoInmueble= TipoInmueble.objects.filter(id=kwargs['pk']).first()
        serializer = TipoInmuebleSerializer(tipoInmueble, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        
    def get(self, request, *args, **kwargs):
        
        tipoInmueble= TipoInmueble.objects.filter(id=kwargs['pk']).first()
        serializer = TipoInmuebleSerializer(tipoInmueble)
        return Response(serializer.data)
    
class AllTipoInmueble(generics.ListAPIView):
    serializer_class = TipoInmuebleSerializer
    model = serializer_class.Meta.model
    paginate_by = 100
    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset