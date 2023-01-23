from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import *


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'is_staff', 'nickname', 'email', 'gender', 'groups']

class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']