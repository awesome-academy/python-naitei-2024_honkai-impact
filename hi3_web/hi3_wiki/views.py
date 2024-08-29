from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static
from django.http import HttpResponse
from django.template import loader
from .forms import *
from .models import *

# Create your views here.

def valkyrie(request):
    my_valks = Valkyrie.objects.all().values()
    my_battlesuits = Battlesuit.objects.all().values()
    template = loader.get_template('all_valkyrie.html')
    context = {
        'my_valks': my_valks,
        'my_battlesuits': my_battlesuits,
    }
    return HttpResponse(template.render(context, request))

def battlesuit_detail(request, valkyrie_name, battlesuit_name):
    my_valks = Valkyrie.objects.get(valkyrie_name=valkyrie_name)
    my_battlesuits = Battlesuit.objects.get(battlesuit_name=battlesuit_name)
    template = loader.get_template('battlesuit_details.html')
    context = {
        'my_valks': my_valks,
        'my_battlesuits': my_battlesuits,
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
    form = search_weapons(request.GET or None)
    query = form.cleaned_data.get('query', '') if form.is_valid() else ''
    
    if query:
        my_weaps = WeaponList.objects.filter(weapon_name=query)
        my_weaps_ranks = WeaponRanks.objects.filter(weapon_name=query)
    else:
        my_weaps = WeaponList.objects.all()
        my_weaps_ranks = WeaponRanks.objects.all()
    
    context = {
        'form': form,
        'my_weaps': my_weaps,
        'my_weaps_ranks': my_weaps_ranks,
        'query': query,
    }
    return render(request, 'weapons.html', context)

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
