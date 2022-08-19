# from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import Project,Event,Gallery,Founder,Technical,Pr,Cc,Graphic,Smo,Sm
# from .forms import ProjectForm
# from . forms import ContactForm

# Create your views here.

def projects(request):
    projects = Project.objects.all()
    events = Event.objects.all()
    galleries = Gallery.objects.all()
    # teams = Team.objects.all()
    context = {'projects': projects,
        'events': events,
        'galleries':galleries,
        # 'teams': teams
    }
    return render(request, "index.html", context)


def ourteams(request):
    founders  = Founder.objects.all()
    technicals = Technical.objects.all()
    ccs = Cc.objects.all()
    graphics = Graphic.objects.all()
    smos = Smo.objects.all()
    prs = Pr.objects.all()
    sms = Sm.objects.all()

    context = {
        'founders' : founders,
        'technicals' : technicals,
        'ccs' : ccs,
        'graphics' : graphics,
        'smos' : smos,
        'sms' : sms,
        'prs' : prs,
    }
    return render (request, "our_team.html", context)

def comingsoon(request):
    return render (request, "comingsoon.html")
