from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import PlayerCharacter, Inventory
from db.models import ItemInfo, Item

def player_hunting(request):
    #이벤트 종료 후 아이템 추가
    playerID, itemID = int(request.POST.get('playerID')), request.POST.get('itemID')
    item_info = ItemInfo.objects.get(itemID=itemID)
    player_character = PlayerCharacter.objects.get(id=playerID)
    player_inventory = Inventory.objects.get(playerCharacter=player_character)
    item = Item(inventory=player_inventory,
                itemID=item_info.itemID,
                itemName=item_info.itemName,
                itemType=item_info.itemType,
                sellingValue=item_info.sellingValue,
                buyingValue=item_info.buyingValue,
                exp=item_info.exp)
    item.save()

    # 이벤트 종료 후 경험치 추가
    player_character.exp += item.exp
    player_character.save()

    return render(request, 'player/player_update.html')

def player_harvesting(request):
    #이벤트 종료 후 아이템 추가
    playerID, itemID = int(request.POST.get('playerID')), request.POST.get('itemID')
    item_info = ItemInfo.objects.get(itemID=itemID)
    player_character = PlayerCharacter.objects.get(id=playerID)
    player_inventory = Inventory.objects.get(playerCharacter=player_character)
    item = Item(inventory=player_inventory,
                itemID=item_info.itemID,
                itemName=item_info.itemName,
                itemType=item_info.itemType,
                sellingValue=item_info.sellingValue,
                buyingValue=item_info.buyingValue,
                exp=item_info.exp)
    item.save()

    # 이벤트 종료 후 경험치 추가
    player_character.exp += item.exp
    player_character.save()

    return render(request, 'player/player_update.html')

def player_taming(request):
    #이벤트 종료 후 아이템 추가
    playerID, itemID = int(request.POST.get('playerID')), request.POST.get('itemID')
    item_info = ItemInfo.objects.get(itemID=itemID)
    player_character = PlayerCharacter.objects.get(id=playerID)
    player_inventory = Inventory.objects.get(playerCharacter=player_character)
    item = Item(inventory=player_inventory,
                itemID=item_info.itemID,
                itemName=item_info.itemName,
                itemType=item_info.itemType,
                sellingValue=item_info.sellingValue,
                buyingValue=item_info.buyingValue,
                exp=item_info.exp)
    item.save()

    # 이벤트 종료 후 경험치 추가
    player_character.exp += item.exp
    player_character.save()

    return render(request, 'player/player_update.html')

def player_farming(request):
    #이벤트 종료 후 아이템 추가
    playerID, itemID = int(request.POST.get('playerID')), request.POST.get('itemID')
    item_info = ItemInfo.objects.get(itemID=itemID)
    player_character = PlayerCharacter.objects.get(id=playerID)
    player_inventory = Inventory.objects.get(playerCharacter=player_character)
    item = Item(inventory=player_inventory,
                itemID=item_info.itemID,
                itemName=item_info.itemName,
                itemType=item_info.itemType,
                sellingValue=item_info.sellingValue,
                buyingValue=item_info.buyingValue,
                exp=item_info.exp)
    item.save()

    # 이벤트 종료 후 경험치 추가
    player_character.exp += item.exp
    player_character.save()

    return render(request, 'player/player_update.html')

@csrf_exempt
def player_fishing(request):
    #이벤트 종료 후 아이템 추가
    playerID, itemID = int(request.POST.get('playerID')), request.POST.get('itemID')
    item_info = ItemInfo.objects.get(itemID=itemID)
    player_character = PlayerCharacter.objects.get(id=playerID)
    player_inventory = Inventory.objects.get(playerCharacter=player_character)
    item = Item(inventory=player_inventory,
                itemID=item_info.itemID,
                itemName=item_info.itemName,
                itemType=item_info.itemType,
                sellingValue=item_info.sellingValue,
                buyingValue=item_info.buyingValue,
                exp=item_info.exp)
    item.save()

    # 이벤트 종료 후 경험치 추가
    player_character.exp += item.exp
    player_character.save()

    return render(request, 'player/player_update.html')

def player_buying(request):
    pass

def player_selling(request):
    pass