from django.shortcuts import render
from django.templatetags.static import static
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
    my_weaps = WeaponList.objects.all()
    my_weaps_ranks = WeaponRanks.objects.all()
    template = loader.get_template('weapons.html')
    context = {
        'my_weaps': my_weaps,
        'my_weaps_ranks': my_weaps_ranks,
    }
    return HttpResponse(template.render(context, request))

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

def test_static(request):
    url = static('img/Key_of_Radiance_4.jpg')
    return HttpResponse(f'<img src="{url}" alt="Test Image">')
