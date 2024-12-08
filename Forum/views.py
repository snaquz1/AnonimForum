from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    updates = Update.objects.all().order_by("-date")[:3]

    return render(request, "main.html", context={"updates": updates})

def updates(request):
    updates = Update.objects.all()

    return render(request, "updates.html", context={"updates": updates})