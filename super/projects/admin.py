from django.contrib import admin
from . models import Project,Event,Gallery,Founder,Technical,Pr,Cc,Graphic,Smo,Sm

@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display=['about','mission']

@admin.register(Event)
class EventModelView(admin.ModelAdmin):
    list_display=['title','body','eve_image']

@admin.register(Gallery)
class GalleryModelAdmin(admin.ModelAdmin):
    list_display=['role','photos']

@admin.register(Founder)
class Founders(admin.ModelAdmin):
    list_display=['name','role','profile_pic','twitter','linkedin','instagram']

@admin.register(Technical)
class Technical(admin.ModelAdmin):
    list_display=['name','role','profile_pic','twitter','linkedin','instagram']

@admin.register(Pr)
class Pr(admin.ModelAdmin):
    list_display=['name','role','profile_pic','twitter','linkedin','instagram']

@admin.register(Graphic)
class Graphic(admin.ModelAdmin):
    list_display=['name','role','profile_pic','twitter','linkedin','instagram']

@admin.register(Cc)
class Cc(admin.ModelAdmin):
    list_display=['name','role','profile_pic','twitter','linkedin','instagram']

@admin.register(Smo)
class Smo(admin.ModelAdmin):
    list_display=['name','role','profile_pic','twitter','linkedin','instagram']

@admin.register(Sm)
class Sm(admin.ModelAdmin):
    list_display=['name','role','profile_pic','twitter','linkedin','instagram']
