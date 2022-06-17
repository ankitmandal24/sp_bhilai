from django.urls import path
from . import views
from .views import contactView, successView

urlpatterns = [
    path('', views.projects, name='projects'),
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),

]
