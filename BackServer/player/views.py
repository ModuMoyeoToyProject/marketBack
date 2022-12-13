from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import PlayerCharacter, Inventory
from db.models import Fish

def player_hunting(request):
    return render(request, 'player/player_update.html')

def player_harvesting(request):
    return render(request, 'player/player_update.html')

def player_taming(request):
    return render(request, 'player/player_update.html')

def player_farming(request):
    return render(request, 'player/player_update.html')

@csrf_exempt
def player_fishing(request):
    playerID = request.POST.get('playerID')
    fishID = request.POST.get('id')
    print(playerID)
    print(PlayerCharacter.objects.get(playerID=playerID).inventory)
    print(Fish.objects.get(fishID=fishID))

    return render(request, 'player/player_update.html')

def player_buying(request):
    pass

def player_selling(request):
    pass