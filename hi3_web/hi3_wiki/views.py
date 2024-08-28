from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def valkyrie(request):
    my_valks = Valkyrie.objects.all().values()
    template = loader.get_template('all_valkyrie.html')
    context = {
        'my_valks': my_valks,
    }
    return HttpResponse(template.render(context, request))

def introduction (request):
    template = loader.get_template('introduction.html')
    return HttpResponse(template.render())

def overall_guide (request):
    pass
    return HttpResponse("Hello Overall guide")

def team_build (request):
    pass
    return HttpResponse("Hello Team Build")

def weapon (request):
    pass

def stigmata (request):
    pass
    return HttpResponse("Hello Stigmata")

def elyrealm (request):
    pass
    return HttpResponse("Hello Elysian Realm")

def abyss (request):
    pass
    return HttpResponse("Hello Abyss")

def ma (request):
    pass
    return HttpResponse("Hello Memorial Arena'")

def details (request, id):
    my_valks = Valkyrie.objects.get(valkyrie_id=id)
    template = loader.get_template('details.html')
    context = {
        'my_valks': my_valks,
    }
    return HttpResponse(template.render(context, request))

def home (request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


