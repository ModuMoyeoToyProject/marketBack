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

