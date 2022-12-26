from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Map
def system_update(request, userSeq):
    return render(request, 'system/system_update.html')
@csrf_exempt
def map_data(request):
    mapID = request.POST.get('mapID')
    map = Map.objects.get(mapID=mapID)
    print(map)
    return render(request, 'system/system_update.html')