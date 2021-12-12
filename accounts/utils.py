from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls.base import reverse
from accounts.forms import UserForm2
from accounts.models import Solicitation
from django.contrib.auth.models import Group, Permission

def ApproveSolicitation(request, pk):
    solicitation = Solicitation.objects.get(pk=pk)
    solicitation.accept = True
    
    my_group, created = Group.objects.get_or_create(name='Empresa') 
    permission = Permission.objects.get(codename = 'add_announcement')
    my_group.permissions.add(permission)
    
    solicitation.user.groups.add(my_group)
    solicitation.save()
    
    return redirect('/accounts/listar_solicitacoes/')

def update_profile(request):
    args = {}
    if request.method == 'POST':
        form = UserForm2(request.POST or None, request.FILES or None,instance = request.user, )
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm2()

    args['form'] = form
    return render(request, 'accounts/edit-user.html', args)
    