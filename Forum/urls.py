from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", main),
    path("updates", updates),
    path("boards", boards),
    re_path(r"^boards/(?P<action>create|delete)$", boardaction),
    path("boards/<str:board_uuid>", boardbyuuid)

]