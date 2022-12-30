from player.models import Character, Inventory
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.http import JsonResponse
from .models import *


@csrf_exempt
def register(request):
    if request.method == 'POST':
        response = dict()
        if request.POST['password1'] == request.POST['password2']:
            try:
                if not User.objects.filter(username=request.POST['username']).exists():
                    new_user = User.objects.create_user(
                        username=request.POST['username'],
                        nickname=request.POST['nickname'],
                        email=request.POST['email'],
                        password=request.POST['password1'],
                    )
                    auth.login(request, new_user)
                    response['result'] = 'Successed'
                    # CreateCharactor(new_user)
                else:
                    response['result'] = 'AlreadyExists'
            except Exception as e:
                print(e)
                response['result'] = 'Failed'
        else:
            response['result'] = 'NotMatchedPassword'
        return JsonResponse(response)

        
    # #인벤토리 생성
        # player_inventory = Inventory(playerCharacter=player_character)
        # print(type(player_inventory))
        # player_inventory.save()

        response['result'] = 'successful'
        return JsonResponse(response)
        # except:
        #     print('no success')
        #     if Account.objects.filter(name=name, id=id, email=email).exists():
        #         response['result'] = 'unsuccessful'
        #         response['type'] = 'user info already exists'
        #         return JsonResponse(response)
        #
        #     response['result'] = 'unsuccessful'
        #     return JsonResponse(response)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        response = dict()
        user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_active:
            auth.login(request, user)
            response['result'] = 'SuccessedLogin'
        else:
            response['result'] = 'FailedLogin'
        return JsonResponse(response)
