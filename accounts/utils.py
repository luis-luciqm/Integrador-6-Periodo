from django.shortcuts import redirect
from authentication.models import User
from django.contrib.auth.models import Group

def UserBusiness(request):
    user = User.objects.get(pk=request.user.pk)
    
    my_group, created = Group.objects.get_or_create(name='Empresa') 
    user.groups.add(my_group)
    
    return redirect('/')