import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BackServer.settings")

import django
django.setup()

from account.models import Account
from player.models import PlayerCharacter, Inventory
#
print(Account.objects.values())
print(PlayerCharacter.objects.values())
print(Inventory.objects.values())
# Account.objects.all().delete()
# PlayerCharacter.objects.all().delete()