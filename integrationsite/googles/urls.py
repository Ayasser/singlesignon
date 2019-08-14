from django.urls import path
from django.conf.urls import url

from . import views
from .views import signin, signout
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^login/', signin ),
    url(r'^logout/', signout ,name="logout"),

]
