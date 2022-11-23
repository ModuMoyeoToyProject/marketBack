from django.shortcuts import render

def player_update(request, userSeq):
    return render(request, 'player/player_update.html')