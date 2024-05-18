
from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("about/", about),
    path("<str:contact_url>",contact,name='contact' ),
]
