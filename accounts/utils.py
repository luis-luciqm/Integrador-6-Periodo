from django.db.models.query_utils import Q
from django.shortcuts import redirect
from accounts.models import Solicitation
from django.contrib.auth.models import Group, Permission

def ApproveSolicitation(request, pk):
    solicitation = Solicitation.objects.get(pk=pk)
    solicitation.accept = True
    
    my_group, created = Group.objects.get_or_create(name='Empresa') 
    permission = Permission.objects.get(codename = 'add_announcement')
    my_group.permissions.add(permission)
    permission = Permission.objects.get(codename = 'change_announcement')
    my_group.permissions.add(permission)
    
    solicitation.user.groups.add(my_group)
    solicitation.save()
    
    return redirect('/accounts/listar_solicitacoes/')