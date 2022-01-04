from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_filter = ['groups']

admin.site.register(User,UserAdmin)
admin.site.register(Skills)