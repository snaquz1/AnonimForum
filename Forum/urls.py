from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", main),
    path("updates", updates),
    path("boards", boards),
    path("boards/<str:board_uuid>", boardbyuuid)
]