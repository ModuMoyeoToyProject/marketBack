from django.db import models
from account.models import Account

class PlayerCharacter(models.Model):
    account = models.ForeignKey('account.Account', on_delete=models.PROTECT)
    statusID = models.CharField(max_length=45, default=1)
    jobID = models.CharField(max_length=45, default=1)
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    title = models.CharField(max_length=45, default=1)

class Status(models.Model):
    PlayerCharacterID = models.ForeignKey('player.PlayerCharacter', on_delete=models.PROTECT)
    Hp = models.IntegerField()
    Mp = models.IntegerField()
    Str = models.IntegerField()
    Dex = models.IntegerField()
    Con = models.IntegerField()
    Attk = models.IntegerField()
    Def = models.IntegerField()
    Hit = models.IntegerField()
    Dodge = models.IntegerField()
    Block = models.IntegerField()
    Critical = models.IntegerField()
    Agility = models.IntegerField()
    Speed = models.IntegerField()
    Friendly = models.IntegerField()
    buffID = models.IntegerField()
    debuffID = models.IntegerField()


class Inventory(models.Model):
    PlayerCharacterID = models.ForeignKey('player.PlayerCharacter', on_delete=models.PROTECT)
    money = models.IntegerField(default=0)
    weight = models.IntegerField(null=True)
    quantity = models.IntegerField(default=0)

# class ItemStored(models.Model):
#     ItemStoredID = models.AutoField(primary_key=True)
#     item = models.ForeignKey('db.Fish', on_delete=models.PROTECT)
#     count = 0
