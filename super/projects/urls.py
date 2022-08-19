from django.urls import path
from . import views
# from .views import contactView, successView

urlpatterns = [
    path('', views.projects, name='about'),
    path('ourteams', views.ourteams, name='ourteams'),
    path('comingsoon', views.comingsoon, name='comingsoon')
]
