import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BackServer.settings")

import django
django.setup()

from account.models import Account
from player.models import PlayerCharacter, Inventory
from db.models import Fish
from system.models import Map
from system.map_init import map_init
import requests
import json

# test_player = Account(id='test', email='test@test', name='a', gender='a', username='test', password='test')
# test_player.save()
#
# playerCharacter = PlayerCharacter(account=test_player)
# playerCharacter.save()
#
# test_inven = Inventory(playerCharacter=PlayerCharacter.objects.get(id=4))
# test_inven.save()

# test_fish = Fish(id='yeah', sellingValue=0, buyingValue=0, exp=0)
# test_fish.save()
# test_inven.item = test_fish
# test_inven.save()

# print(Account.objects.values())
# print(PlayerCharacter.objects.values())
# print(Inventory.objects.values())
# print(Fish.objects.values())
map_init()
print(Map.objects.values())

# Inventory.objects.all().delete()
# PlayerCharacter.objects.all().delete()
# Account.objects.all().delete()


#
# example = {'fishID': '#fish008',
#            'name': '참돔',
#            'selling_value': 300,
#            'buying_value': 0,
#            'exp': 3,
#            'playerID': 2}
# response = requests.post('http://127.0.0.1:8000/game/player/action/fishing', example)
# print(response)

example = {'mapID': 1}
response = requests.post('http://127.0.0.1:8000/game/system/mapdata', example)
print(response)

