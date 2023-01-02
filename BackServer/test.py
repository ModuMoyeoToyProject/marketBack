import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BackServer.settings")

import django
django.setup()

from account.models import Account, User
from player.models import PlayerCharacter, Inventory
from db.models import ItemInfo, Item, NPC, Dialogue
from system.models import Map
from system.map_init import map_init
import requests
import json


# test_account = Account.objects.get(accountID=1)
# print(test_account)
#
# test_character = PlayerCharacter(account=test_account,
#                                  statusID='test',
#                                  jobID='test',
#                                  location='test_location')
# test_character.save()


# test_inven = Inventory(PlayerCharacterID=PlayerCharacter.objects.get(id=2))
# test_inven.save()
# print(Inventory.objects.values().get(id=1))

# test_item_farming = ItemInfo(itemID='#farm001',
#                              itemName='배추',
#                              itemType='농사',
#                              sellingValue=50,
#                              buyingValue=50,
#                              exp=1)

# print(ItemInfo.objects.values().get(itemID='#farm001'))

response = requests.post('http://127.0.0.1:8000/game/player/action/farming', json={'message': 'event!!!',
                                                                                   'PlayerCharacterID': 2,
                                                                                   'itemID': '#farm001'})
print(response)