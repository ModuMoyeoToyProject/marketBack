from django.shortcuts import render

def player_hunting(request, userSeq):
    return render(request, 'player/player_update.html')

def player_harvesting(request, userSeq):
    return render(request, 'player/player_update.html')

def player_taming(request, userSeq):
    return render(request, 'player/player_update.html')

def player_farming(request, userSeq):
    return render(request, 'player/player_update.html')

def player_fishing(request, userSeq):
    return render(request, 'player/player_update.html')