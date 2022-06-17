from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import Project,Event,Gallery,Team
# from .forms import ProjectForm
from . forms import ContactForm

# Create your views here.

def projects(request):
    projects = Project.objects.all()
    events = Event.objects.all()
    galleries = Gallery.objects.all()
    teams = Team.objects.all()
    context = {'projects': projects,
        'events': events,
        'galleries':galleries,
        'teams': teams
    }
    return render(request, "index.html", context)


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['ankitmandal244@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
