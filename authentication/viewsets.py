from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from rest_framework.response import Response


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        
        my_group = Group.objects.get(name='Normal') 
        user.groups.add(my_group)
        
        token = RefreshToken.for_user(user).access_token
    
        return Response(user_data, status=status.HTTP_200_OK)