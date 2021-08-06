from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from account.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['id'] = account.id
            data['email'] = account.email
           
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            
            'id': user.pk,
            'email': user.email,
            'token': token.key,
            
        })
        

    def get(self, request):
        try:
            account = request.user
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = {}
        if request.method == 'GET':
           data['id'] = account.id,
        data['email'] = account.email
        return Response(data)
