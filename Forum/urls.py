from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", main),
    path("updates", updates),
    path("boards", boards),
    path("boards/create", boardcreation),
    path("boards/<str:board_uuid>", boardbyuuid),
    path("boards/info/<int:board_id>", boardinfo)

]