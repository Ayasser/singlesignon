import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from google import models
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render
from .models import User
from django.contrib.auth import logout as auth_logout



def index(request):
    context = {
        'posts': User.objects.order_by('-date')
        if request.user.is_authenticated else []
    }

    return render(request, 'google/index.html', context)
def logout(request):
    auth_logout(request)
    return redirect('/')