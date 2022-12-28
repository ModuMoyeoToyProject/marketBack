from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Map
from db.models import Dialogue
import json


def system_update(request, userSeq):
    return render(request, 'system/system_update.html')

@csrf_exempt
def map_data(request):
    if request.method == 'GET':
        return render(request, 'system/system_update.html')

    mapID = request.POST.get('mapID')
    map_obj = Map.objects.get(mapID=mapID)

    map_data = dict()
    map_data['mapID'] = map_obj.mapID
    map_data['location'] = map_obj.location
    map_data['required_level'] = map_obj.required_level
    map_data['coordinate'] = map_obj.coordinate
    map_data['street'] = map_obj.street

    return JsonResponse(map_data)


@csrf_exempt
def script_data(request):
    if request.method == 'GET':
        return render(request, 'system/system_update.html')

    post_data = json.loads(request.body)
    dialogueID = post_data.get('dialogueID')
    dialogue_obj = Dialogue.objects.get(id=int(dialogueID))

    dialogue_data = dict()
    dialogue_data['dialogueID'] = dialogue_obj.id
    dialogue_data['mainCategory'] = dialogue_obj.mainCategory
    dialogue_data['middleCategory'] = dialogue_obj.middleCategory
    dialogue_data['subCategory'] = dialogue_obj.subCategory
    dialogue_data['questMode'] = dialogue_obj.questMode
    dialogue_data['scene'] = dialogue_obj.scene
    dialogue_data['dialogue'] = dialogue_obj.dialogue

    return JsonResponse(dialogue_data)
