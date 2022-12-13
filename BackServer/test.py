import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BackServer.settings")

import django
django.setup()

from account.models import Account
from player.models import PlayerCharacter, Inventory
from db.models import Fish
import requests
import json

# test_player = Account(id='test', email='test@g', name='testy', gender='female', username='TEST', password='TESTY')
# test_player.save()
#
# playerCharacter = PlayerCharacter()
# playerCharacter.save()
# test = Account(id='test', email='test@test', name='test', gender='test', username='test', password='test', playerCharacter=playerCharacter)
# test.save()
print(Account.objects.values())
print(PlayerCharacter.objects.values())
print(Inventory.objects.values())
#
# Account.objects.all().delete()
# PlayerCharacter.objects.all().delete()
# Inventory.objects.all().delete()

# fish = Fish(fishID='#fish008', fishName='참돔', sellingValue=300, buyingValue=0, exp=3)
# fish.save()
# print(Fish.objects.values())
#
# example = {'id': '#fish008',
#            'name': '참돔',
#            'selling_value': 300,
#            'buying_value': 0,
#            'exp': 3,
#            'playerID': 3}
# response = requests.post('http://127.0.0.1:8000/game/player/action/fishing', example)
# print(response)