from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import *
from player.models import *


class Skill(models.Model):
    name = models.CharField(verbose_name='스킬명', max_length=16, unique=True)
    description = models.CharField(verbose_name='설명', max_length=64, blank=True)
    hp_consumption = models.IntegerField(verbose_name='체력 소비량', default=0)
    mp_consumption = models.IntegerField(verbose_name='마나 소비량', default=0)
    cooldown_time = models.IntegerField(verbose_name='재사용 대기시간(ms)', default=1000)
    activation_time = models.IntegerField(verbose_name='시연시간(ms)', default=500)
    effect = models.CharField(verbose_name='스킬효과', max_length=16, blank=True)
    # owners = models.ForeignKey(User, verbose_name='보유자', blank=True, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = '스킬'
        verbose_name_plural = verbose_name

class Job(models.Model):
    name = models.CharField(verbose_name='직업', max_length=16, primary_key=True)
    description = models.CharField(verbose_name='설명', max_length=64, blank=True)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "직업"
        verbose_name_plural = verbose_name

class Itemtype(models.Model):
    name = models.CharField(verbose_name='타입명', max_length=16, primary_key=False)
    description = models.CharField(verbose_name='설명', max_length=64, blank=True)
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = '아이템 타입'
        verbose_name_plural = verbose_name

class Item(models.Model):
    name = models.CharField(verbose_name='아이템명', max_length=16, unique=True)
    description = models.CharField(verbose_name='설명', max_length=64, blank=True)
    # inventory = models.ForeignKey('player.inventory', on_delete=models.PROTECT, null=True)
    # itemID = models.CharField(max_length=45)
    # type = models.ForeignKey(Itemtype, verbose_name='아이템 타입', on_delete=models.PROTECT)
    purchase_price = models.IntegerField(verbose_name='구입 가격', default=0)
    sell_price = models.IntegerField(verbose_name='판매 가격', default=0)
    # exp = models.IntegerField(default=0)
    # count = models.IntegerField(verbose_name='수량', default=1)
    weight = models.IntegerField(verbose_name='무게', default=1)
    # owners = models.ForeignKey(User, verbose_name='보유자', blank=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = '아이템'
        verbose_name_plural = verbose_name

class ItemInfo(models.Model):
    itemID = models.CharField(max_length=255, primary_key=True)
    itemName = models.CharField(max_length=45)
    itemType = models.CharField(max_length=45)
    sellingValue = models.IntegerField(default=0)
    buyingValue = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)

class Fish(models.Model):
    fishName = models.CharField(max_length=255)
    selling_value = models.IntegerField()
    buying_value = models.IntegerField()
    exp = models.IntegerField()
    location = models.CharField(max_length=255)
    catchRate = models.IntegerField()

class Seed(models.Model):
    seedName = models.CharField(max_length=255, unique=True)
    relatedItemID = models.CharField(max_length=255)

class NPC(models.Model):
    npcID = models.CharField(max_length=45, primary_key=True)
    npcName = models.CharField(max_length=45)
    npcType = models.CharField(max_length=45)
    npcImgPath = models.CharField(max_length=45)

class Dialogue(models.Model):
    npc = models.ForeignKey('db.NPC', on_delete=models.PROTECT)
    mainCategory = models.CharField(max_length=255)
    middleCategory = models.CharField(max_length=255)
    subCategory = models.CharField(max_length=255)
    questMode = models.BooleanField()
    scene = models.CharField(max_length=255)
    dialogue = models.TextField()

class NoneActingObject(models.Model):
    objectID = models.CharField(max_length=45, primary_key=True)
    objectName = models.CharField(max_length=45)
    objectType = models.CharField(max_length=45)
    objectEffect = models.CharField(max_length=45)

class Building(models.Model):
    buildingID = models.CharField(max_length=45, primary_key=True)
    buildingName = models.CharField(max_length=45)
    mapID = models.CharField(max_length=45)
    buildingImgPath = models.CharField(max_length=45)
    darkModeYn = models.CharField(max_length=45)
