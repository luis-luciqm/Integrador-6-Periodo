from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model= Group
        fields = ('id','name')

class LoginSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    fullname = serializers.CharField(read_only=True)
    groups = GroupSerializer(many=True, read_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['id','email', 'password', 'username','fullname','image','tokens','groups']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        # if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
        #     raise AuthenticationFailed(
        #         detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

        if not user:
            raise AuthenticationFailed('Credenciar erradas, tente norvamente.')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        ##if not user.is_verified:
          ##  raise AuthenticationFailed('Email is not verified')

        return {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens,
            'fullname': user.fullname,
            'image' : user.image,
            'groups': user.groups
        }

        return super().validate(attrs)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=70,min_length=6,write_only=True)

    class Meta:
        model = User
        fileds = ['email', 'username', 'password']
        exclude = ('updated','created', 'fullname')

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    
