import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BackServer.settings")

import django
django.setup()

from account.models import Account
from player.models import PlayerCharacter, Inventory
from db.models import ItemInfo, Item, NPC, Dialogue
from system.models import Map
from system.map_init import map_init
import requests
import json

# exmp_npc = NPC(
#     npcID = 'exampleNPC',
#     npcName = 'exampleNPC',
#     npcType = 'example',
#     npcImgPath = 'example_path'
# )
# exmp_npc.save()

# with open('script_example.txt', 'r', encoding='utf-8') as script:
#     d = ''
#     for line in script.readlines():
#         line = '|'.join(line.split('|')).strip() + '||'
#         d += line + '\n'
#
#     exmp_dia = Dialogue(
#         npc=NPC.objects.get(npcID='exampleNPC'),
#         type='example dialogue',
#         dialogue=d
#     )
#
#     exmp_dia.save()

# print(NPC.objects.all())
# print(Dialogue.objects.values())
response = requests.post('http://127.0.0.1:8000/game/system/scriptdata', json={'dialogueID': 2})
print(response.text)