from django.shortcuts import render

def player_hunting(request):
    return render(request, 'player/player_update.html')

def player_harvesting(request):
    return render(request, 'player/player_update.html')

def player_taming(request):
    return render(request, 'player/player_update.html')

def player_farming(request):
    return render(request, 'player/player_update.html')

def player_fishing(request):
    return render(request, 'player/player_update.html')