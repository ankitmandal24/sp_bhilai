from django.db import models

# Create your models here.
class Project(models.Model):

    about = models.TextField(null=True, blank=True)
    mission = models.TextField(null=True, blank=True)
class Event(models.Model):


    eve_image = models.ImageField(null=True, blank=True,)
    body = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    tag = models.CharField(max_length=200, null=True, blank=True)



class Gallery(models.Model):
    role = models.CharField(max_length=200)
    photos = models.ImageField(null=True, blank=True,)
    title = models.TextField(blank=True, null=True)
    extra_title = models.CharField(max_length=200, null=True)


class Founder(models.Model):
    name = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=500, null=True, blank=True)

class Technical(models.Model):
    name = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=500, null=True, blank=True)


class Pr(models.Model):
    name = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=500, null=True, blank=True)

class Cc(models.Model):
    name = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=500, null=True, blank=True)

class Graphic(models.Model):
    name = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=500, null=True, blank=True)

class Smo(models.Model):
    name = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=500, null=True, blank=True)


class Sm(models.Model):
    name = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=500, null=True, blank=True)
