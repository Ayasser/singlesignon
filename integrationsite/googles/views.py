import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.urls import reverse
from django.contrib import admin 
from django.contrib.auth.models import User 
from django.db import models
from google.oauth2 import id_token
from google.auth.transport import requests
import json
from apiclient import discovery
from oauth2client import client
from .models import User, UserGoogle
from django.contrib.auth import login, logout

def index(request):
    context = {
        'posts': User.objects.order_by('-date')
        if request.user.is_authenticated else []
    }
    return render(request, 'googles/index.html', context)



def signin(request):
    # (Receive auth_code by HTTPS POST)
    # auth_code = request.query_params.get('code')
    auth_code = request.GET.get('code')
    print(auth_code)

    CLIENT_SECRET_FILE = '/home/ayasser/Desktop/GitHub/singlesignon/client_secret.json'

    # Exchange auth code for access token, refresh token, and ID token
    credentials = client.credentials_from_clientsecrets_and_code(
        CLIENT_SECRET_FILE,
        [ 'profile', 'email'],
        auth_code)
    print('cred',credentials.access_token,credentials.refresh_token)


    userid = credentials.id_token['sub']
    email = credentials.id_token['email']
    first_name = credentials.id_token['given_name']
    last_name = credentials.id_token['family_name']
    user = User.objects.filter(username=email).first()

    if(user is None):
        user = User.objects.create_user(email,email,first_name=first_name,last_name=last_name)
    # elif(UserGoogle.objects.filter(uid=userid)is None):
    #     user_google = UserGoogle.objects.create(user=user,provider='google',uid=userid)
    #     print('user_google',user_google)
    login(request,user)
    return HttpResponseRedirect('/')

def signout(request):
    logout(request)
    return HttpResponseRedirect('/') 
