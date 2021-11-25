from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from announcement.models import *

# def user_gains_perms(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     # any permission check will cache the current set of permissions
#     user.has_perm('Announcement.change_announcement')
#     user.has_perm('Announcement.delete_announcement')
#     user.has_perm('Announcement.add_announcement')
#     user.has_perm('Announcement.view_announcement')

#     content_type = ContentType.objects.get_for_model(Announcement)
#     permission = Permission.objects.get(
#         codename='change_blogpost',
#         content_type=content_type,
#     )
#     user.user_permissions.add(permission)