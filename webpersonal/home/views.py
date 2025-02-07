from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

from .models import Proyect
# Create your views here.
def home(request):
    name = 'Antony de la Cruz'
    career = 'Backend Developer'
    context = { 
        "name": name,
        "career": career
    }
    return render(request, 'home/index.html', context)


def contact(request):
    return render(request,  'home/contact.html')

def  projects(request):
    projects = Proyect.objects.all().order_by('-id')[:5]
    context = {
        "projects": projects,
    }
    return render(request, 'home/projects.html', context)

def about(request):
    name = 'Marco Antonio'
    description = 'Soy un estudiante de la carrera de ingenieria de software de 5 Cuatrimestre'
    context = {
    "name": name,
    "description": description
    }
    return render(request, 'home/about.html', context)