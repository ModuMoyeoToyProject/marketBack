from django.shortcuts import render
from player.models import PlayerCharacter, Inventory
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import Account

@csrf_exempt
def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        gender = request.POST.get('sex')
        username = request.POST.get('name')
        id = request.POST.get('id')
        password = request.POST.get('psw')
        email = request.POST.get('email')

        response = dict()
        if Account.objects.filter(name=name, id=id, email=email).exists():
            response['result'] = 'unsuccessful'
            response['type'] = 'user info already exists'
            return JsonResponse(response)
        else:
            #계정 생성
            register_account = Account(username=username,
                                       gender=gender,
                                       name=name,
                                       id=id,
                                       password=password,
                                       email=email)
            register_account.save()

            #캐릭터 생성
            player_character = PlayerCharacter(account=register_account)
            print(type(player_character))
            player_character.save()

            #인벤토리 생성
            player_inventory = Inventory(playerCharacter=player_character)
            print(type(player_inventory))
            player_inventory.save()

            response['result'] = 'successful'
            return JsonResponse(response)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        id = request.POST.get('username')
        password = request.POST.get('psw')

        response = dict()
        if Account.objects.filter(id=id, password=password).exists():
            response['result'] = 'successful'
            return JsonResponse(response)
        else:
            response['result'] = 'unsuccessful'
            response['type'] = 'typed info unmatched'
            return JsonResponse(response)



