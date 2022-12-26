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
    fishID, fishName = request.POST.get('fishID'), request.POST.get('name')
    sellingValue, buyingValue, exp = request.POST.get('selling_value'), request.POST.get('buying_value'), request.POST.get('exp')
    player_inventory = Inventory.objects.get(playerCharacter_id=playerID)

    if Fish.objects.get(inventory=Inventory.objects.get(playerCharacter_id=playerID)):
        fish = Fish.objects.get(inventory=Inventory.objects.get(playerCharacter_id=playerID))
        fish.count += 1
        fish.save()
    else:
        fish = Fish(fishID=fishID, fishName=fishName, sellingValue=sellingValue, buyingValue=buyingValue, exp=exp, inventory=player_inventory)
        fish.save()

    return render(request, 'player/player_update.html')

def player_buying(request):
    pass

def player_selling(request):
    pass