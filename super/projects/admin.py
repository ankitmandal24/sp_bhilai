from django.contrib import admin

# Register your models here
from . models import Project,Event,Gallery,Team

admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(Team)
