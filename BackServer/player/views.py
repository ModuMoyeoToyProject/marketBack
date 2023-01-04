from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PlayerCharacter, Inventory
from db.models import ItemInfo, Item, Seed
import json

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

@csrf_exempt
def player_farming(request):
    if request.method == 'POST':
        event = json.loads(request.body)

        PlayerCharacterID, seedName = event['PlayerCharacterID'], event['seedName']
        player_character = PlayerCharacter.objects.get(id=PlayerCharacterID)
        player_inventory = Inventory.objects.get(PlayerCharacterID=player_character)

        seed = Seed.objects.get(seedName=seedName)

        item_info = ItemInfo.objects.get(itemID=seed.relatedItemID)
        print(item_info)

        if Item.objects.filter(inventory=player_inventory, itemID=item_info.itemID).exists():
            item = Item.objects.get(inventory=player_inventory, itemID=item_info.itemID)
            item.count += 1
            item.save()
        else:
            item = Item(inventory=player_inventory,
                        itemID=item_info.itemID,
                        itemName=item_info.itemName,
                        itemType=item_info.itemType,
                        sellingValue=item_info.sellingValue,
                        buyingValue=item_info.buyingValue,
                        exp=item_info.exp)
            item.save()

        response = dict()
        response['player_location'] = player_character.location
        response['player_level'] = player_character.level
        try:
            inventory = Item.objects.filter(inventory=player_inventory).all()
            item_list = ''
            for inventory_item in inventory:
                result = f'{inventory_item.itemName},{inventory_item.count},{inventory_item.buyingValue}/'
                item_list += result
            response['player_inventory'] = item_list
        except:
            response['player_inventory'] = 'No items'
        response['player_item_add'] = item.itemName
        response['player_item_lost'] = seed.seedName

    return JsonResponse(data=response)

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

@csrf_exempt
def player_buying(request):
    if request.method == 'POST':
        response = dict()
        Buying_itemID = request.POST['ItemID']
        PlayerCharacterID = request.POST['PlayerCharacterID']
        player_character = PlayerCharacter.objects.get(id=PlayerCharacterID)
        player_inventory = Inventory.objects.get(PlayerCharacterID=player_character)
        item_info = ItemInfo.objects.get(itemID=Buying_itemID)
        response['Bmoney'] = player_inventory.money
        
        if player_inventory.money >= item_info.buyingValue:
            if Item.objects.filter(inventory=player_inventory, itemID=Buying_itemID).exists():
                item = Item.objects.get(inventory=player_inventory, itemID=Buying_itemID)
                response['Bitem'] = item.count
                item.count += 1
                player_inventory.money-=item_info.buyingValue
                item.save()
                player_inventory.save()
                response['Aitem'] = item.count
            else:
                item = Item(inventory=player_inventory,
                            itemID=item_info.itemID,
                            itemName=item_info.itemName,
                            itemType=item_info.itemType,
                            sellingValue=item_info.sellingValue,
                            buyingValue=item_info.buyingValue,
                            exp=item_info.exp)
                player_inventory.money-=item_info.buyingValue
                player_inventory.save()
                item.save()
                response['Nitem'] = item.count
            response['result'] = 'Successed'
            response['Amoney'] = player_inventory.money
        else:
            response['result'] = 'NotEnoughMoney'
            response['Amoney'] = player_inventory.money
        return JsonResponse(response)
    
@csrf_exempt
def player_selling(request):
    if request.method == 'POST':
        response = dict()
        selling_itemID = request.POST['ItemID']
        PlayerCharacterID = request.POST['PlayerCharacterID']
        player_character = PlayerCharacter.objects.get(id=PlayerCharacterID)
        player_inventory = Inventory.objects.get(PlayerCharacterID=player_character)
        response['Bmoney'] = player_inventory.money
        if Item.objects.filter(inventory=player_inventory, itemID=selling_itemID).exists():
            if Item.objects.get(inventory=player_inventory, itemID=selling_itemID).count > 0:
                item_info = ItemInfo.objects.get(itemID=selling_itemID)
                item = Item.objects.get(inventory=player_inventory, itemID=selling_itemID)
                response['Bitem'] = item.count
                item.count -= 1
                player_inventory.money+=item_info.sellingValue
                item.save()
                player_inventory.save()
                response['Aitem'] = item.count
                response['result'] = 'Successed'
                response['Amoney'] = player_inventory.money
            else:
                response['result'] = 'DontHaveItem'
        else:
            response['result'] = 'ItemDoesNotExists'
        response['Amoney'] = player_inventory.money
        return JsonResponse(response)