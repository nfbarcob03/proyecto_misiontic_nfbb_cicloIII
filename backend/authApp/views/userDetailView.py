from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

from authApp.models.inmueble import Inmueble
from authApp.serializers.inmuebleSerializer import InmuebleSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)

class UserInmueblesDetailView(generics.RetrieveAPIView):
    
    def get(self, request, *args, **kwargs):
        queryset = Inmueble.objects.all()
        id_user_body = kwargs['pk']

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != id_user_body:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        inmueble= Inmueble.objects.filter(id_arrendatario=kwargs['pk'])

        if inmueble.count()<1:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = InmuebleSerializer(inmueble, many=True)
            return Response(serializer.data)


class AllUsers(generics.ListAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    paginate_by = 100
    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset
