from rest_framework.serializers import ModelSerializer
from .models import *


class CharacterSerializer(ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'