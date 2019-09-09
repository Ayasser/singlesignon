from django.urls import path
from django.conf.urls import url

from . import views
from .views import logout

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^logout/', logout ,name="logout"),

]
