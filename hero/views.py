from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.


def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'hero/index.html', context)

def detail(request, hero_id):
    selected_hero = Superhero.objects.get(pk=hero_id)
    context = {
        "selected_hero": selected_hero
    }
    return render(request, 'Superhero/detail.html', context)
    

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego_name = request.POST.get('alter_ego_name')
        primary_super_ability = request.POST.get('primary_super_ability')
        secondary_super_ability = request.POST.get('secondary_super_ability')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego_name=alter_ego_name, primary_super_ability=primary_super_ability, secondary_super_ability=secondary_super_ability, catchphrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superhero:index'))
    else:
        return render(request, 'Superhero/create.html')

def edit(request, hero_id):
    selected_hero = Superhero.objects.get(pk=hero_id)
    if request.method == "POST":
        selected_hero.name = request.POST.get('name')
        selected_hero.alter_ego_name = request.POST.get('alter_ego_name')
        selected_hero.primary_super_ability = request.POST.get('primary_super_ability')
        selected_hero.secondary_super_ability = request.POST.get('secondary_super_ability')
        selected_hero.catchphrase = request.POST.get('catchphrase')
        selected_hero.save()
        context = {
            "selected_hero": selected_hero
        }
        return render(request, 'Superhero/detail.html', context)
    else:
        context = {
            "selected_hero": selected_hero
        }
        return render(request, 'Superhero/edit.html', context)

def delete(request, hero_id):
    selected_hero = Superhero.objects.get(pk=hero_id)
    if request.method == "POST":
        selected_hero.delete()
        return index(request)
    else:
        context = {
            "selected_hero": selected_hero
        }
        return render(request, 'Superhero/delete.html', context)

