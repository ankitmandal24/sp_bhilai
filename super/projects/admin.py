from django.contrib import admin
from . models import Project,Event,Gallery,Team

@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display=['about','mission']

@admin.register(Event)
class EventModelView(admin.ModelAdmin):
    list_display=['title','body','eve_image']

@admin.register(Gallery)
class GalleryModelAdmin(admin.ModelAdmin):
    list_display=['role','photos']

@admin.register(Team)
class TeamModelAdmin(admin.ModelAdmin):
    list_display=['name','role','profile_pic','twitter','linkedin','instagram','github']