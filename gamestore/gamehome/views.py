from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from astroid import objects
from gamehome.models import Game_type,Game
# Create your views here.
def showgame(request):
    game_type = Game_type.objects.all()
    game = Game.objects.all()


    # action = []
    # count = 0
    # for i in game:
    #     if i.game_type_id == 1 and count < 4:
    #         action.append(i)
    #         count = count+1
    # print(action)

    #     if i.game_type_id == count:
    #         action_list.append(i.name)
    #         developer_list.append(i.developer)
    #         count = count + 1 
    #     print(action_list)
    #     print(developer_list)
    # print(action_list)


    
    print(game_type)
    return render(request, 'gamehome/game.html',context={
        'game_type' : game_type,
        'game' : game,
        # 'action' : action,
    })

def seemore(request, seemore):

    g = Game.objects.all()
    list_game = []
    for i in g:
        if i.game_type_id == seemore:
            list_game.append(i)
    print(list_game)
    return render(request, 'gamehome/mygame.html', context={
        'list_game' : list_game,
    })

def search(request):
    search_txt = request.POST.get('searchinput','')
    show_game = Game.objects.filter(
        name__icontains=search_txt
    )
    return render(request, 'gamehome/game.html', {
        'show_game' : show_game
    })

# def photp(request):
#     try:
#         picture = request.FILES['picture']
#     except:
#         picture = None

#     if picture != None:


# def show_all_detail(request, show_all_detail):
#     g = Game.objects.all()
    
#     list_game = []
#     for i in g:
#         if i.game_type_id == show_all_detail:
#             list_game.append(i)

#     return render(request, 'gamehome/mygame.html', context={
#         'list_game' : list_game,
#     })

# def show_information(request, show_information):
#     g = Game.objects.all()
    
#     information = []
#     for o in g:
#         if o.game_id == show_information:
#             show_information.append(o)

#     return render(request, 'gamehome/showgame.html', context={
#         'information' : information,
#     })

def detail(request, detail):
    g = Game.objects.get(pk=detail)
    print(g)
    # list_detail = []

    # for o in g:
    #     if o.game_id == detail:
    #         list_detail.append(o)
    # print(list_detail)
    return render(request, 'gamehome/showgame.html', context={
        # 'list_detail' : list_detail
        'g' : g
    })        

