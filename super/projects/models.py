from django.db import models

# Create your models here.
class Project(models.Model):

    about = models.TextField(null=True, blank=True)
    mission = models.TextField(null=True, blank=True)
class Event(models.Model):

    #owner =
    eve_image = models.ImageField(null=True, blank=True,)
    body = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)


class Gallery(models.Model):
    role = models.CharField(max_length=200)
    photos = models.ImageField(null=True, blank=True,)


class Team(models.Model):
    name = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=500, null=True, blank=True)
    github = models.CharField(max_length=500, null=True, blank=True)




    def __str__(self):
        return self.role
