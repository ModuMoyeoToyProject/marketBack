from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import *
from db.models import *



class Character(models.Model):
    user = models.ForeignKey(User, verbose_name='사용자 이름', on_delete=models.CASCADE)
    level = models.IntegerField(verbose_name='레벨', default=1)
    exp = models.IntegerField(verbose_name='경험치', default=0)
    # job = models.ForeignKey(Job, verbose_name='직업', on_delete=models.PROTECT)
    # statusID = models.CharField(max_length=45, default=1)
    # jobID = models.CharField(max_length=45, default=1)
    # title = models.CharField(max_length=45, default=1) # ??

    def __str__(self) -> str:
        return self.user.nickname
    class Meta:
        verbose_name = "캐릭터"
        verbose_name_plural = verbose_name

class Status(models.Model):
    character = models.OneToOneField(Character, verbose_name='사용자 이름', on_delete=models.CASCADE, primary_key=True)
    # statusID = models.CharField(max_length=45, primary_key=True)
    hp = models.IntegerField(verbose_name='체력', default=100)
    mp = models.IntegerField(verbose_name='마나', default=0)
    Str = models.IntegerField(default=0)
    Dex = models.IntegerField(default=0)
    Con = models.IntegerField(default=0)
    Attk = models.IntegerField(default=0)
    Def = models.IntegerField(default=0)
    Hit = models.IntegerField(default=0)
    Dodge = models.IntegerField(default=0)
    Block = models.IntegerField(default=0)
    Critical = models.IntegerField(default=0)
    Agility = models.IntegerField(default=0)
    Speed = models.IntegerField(default=0)
    Friendly = models.IntegerField(default=0)
    buffID = models.IntegerField(default=0)
    debuffID = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.character.user.nickname
    class Meta:
        verbose_name = "상태"
        verbose_name_plural = verbose_name




class Inventory(models.Model):
    character = models.OneToOneField(Character, verbose_name='가방 소유자', on_delete=models.CASCADE, primary_key=True)
    capacity = models.IntegerField(verbose_name='가방 용량', default=25)
    usage = models.IntegerField(verbose_name='현재 사용량', default=0)
    # weight = models.IntegerField(default=0) # TODO ????
    # quantity = models.IntegerField(default=25) # TODO ???
    # items = models.ManyToManyField(Item, verbose_name='보유 아이템', related_name='items_belonging_to', blank=True)#, on_delete=models.PROTECT, primary_key=False)
    items = models.ManyToManyField(Item, through='ItemAmount', verbose_name='보유 아이템', related_name='items_belonging_to', blank=True)#, on_delete=models.PROTECT, primary_key=False)

    def __str__(self) -> str:
        return self.character.user.nickname
    class Meta:
        verbose_name = "가방"
        verbose_name_plural = verbose_name

class ItemAmount(models.Model):
    inventory = models.ForeignKey(Inventory, verbose_name='소유자', related_name='inventory_of', on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, verbose_name='아이템', related_name='item_belonging_to', on_delete=models.CASCADE, null=True, blank=True)
    item_amount = models.IntegerField(verbose_name='수량', default=1)
    
    def __str__(self) -> str:
        return ''
    
class ItemStored(models.Model):
    ItemStoredID = models.AutoField(primary_key=True)
    # item = models.ForeignKey('db.Fish', on_delete=models.PROTECT)
    count = 0
