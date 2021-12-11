from django.contrib import admin
from .models import *
# Register your models here.
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Announcement, AnnouncementAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(City,CityAdmin)


class ParticipateAnnounceAdmin(admin.ModelAdmin):
    list_display = ['user','announcement']
admin.site.register(ParticipateAnnounce,ParticipateAnnounceAdmin)