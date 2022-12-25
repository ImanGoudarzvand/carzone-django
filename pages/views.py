from django.shortcuts import render
from .models import Team

def home(request):
    queryset = Team.objects.all()
    return render(request, 'pages/home.html', {'teams': list(queryset)})

def about(request):
    queryset = Team.objects.all()
    return render(request, 'pages/about.html', {'teams': list(queryset)})

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
