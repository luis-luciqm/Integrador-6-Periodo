from rest_framework import serializers
from authentication.models import User

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('__all__')