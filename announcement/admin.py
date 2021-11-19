from django.contrib import admin
from .models import *
# Register your models here.
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Announcement, AnnouncementAdmin)