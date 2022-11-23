from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UserForm
from .models import User
from django.core.serializers.json import DjangoJSONEncoder
import json

def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        new_user = form.save()
        return redirect('userInfo')
    else:
        form = UserForm()
        context = dict()
        context['form'] = form
        return render(request, 'user/user_register_form.html', context=context)

def display_user(request):
    context = dict()

    user_info = User.objects.values()
    user_info = json.dumps(list(user_info), cls=DjangoJSONEncoder)

    return JsonResponse(user_info, safe=False)