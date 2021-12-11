from .serializers import *
from rest_framework import generics
from accounts.models import *

class CompanyListViewSet(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        queryset = User.objects.filter(groups__name__in=['Empresa'])
        return queryset