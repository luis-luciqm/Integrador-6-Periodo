from django.shortcuts import redirect
from accounts.models import Solicitation
from django.contrib.auth.models import Group

def ApproveSolicitation(request, pk):
    solicitation = Solicitation.objects.get(pk=pk)
    solicitation.accept = True
    my_group, created = Group.objects.get_or_create(name='Empresa') 
    solicitation.user.groups.add(my_group)
    
    solicitation.save()
    return redirect('/accounts/listar_solicitacoes/')