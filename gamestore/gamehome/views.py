from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from astroid import objects
from gamehome.models import Game_type
# Create your views here.
def gamehome(request):
    mod = ['Action', 'Adventure']
    return render(request ,'gamehome/game.html', context={
        'mod' : mod,
        
    })
def showgame(request):
    game_type = Game_type.objects.all()

    return render(request, 'gamehome/game.html',context={
        'game_type' : game_type,
    })