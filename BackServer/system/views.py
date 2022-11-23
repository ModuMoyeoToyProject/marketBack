from django.shortcuts import render

def system_update(request, userSeq):
    return render(request, 'system/system_update.html')
