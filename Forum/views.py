from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def main(request):
    updates = Update.objects.all().order_by("-date")[:3]
    return render(request, "main.html", context={"updates": updates})

def updates(request):
    updates = Update.objects.all()
    return render(request, "updates.html", context={"updates": updates})

def boards(request):
    boards = Board.objects.all().order_by("-creation_date")
    return render(request, "boards.html", context={"boards": boards})

def boardbyuuid(request, board_uuid):
    global board, messages
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message.objects.create(text=form.cleaned_data["text"])
            message.save()
            board = Board.objects.get(uuid=board_uuid)
            board.messages_uuids += f"{message.uuid}, "
            board.save()
            return HttpResponseRedirect("/boards")

    else:
        form = MessageForm()
        board = Board.objects.get(uuid=board_uuid)
        messages_uuids = board.messages_uuids.split(", ")
        messages = Message.objects.filter(uuid__in=messages_uuids).order_by("datetime")
        print(messages)
    return render(request, "board.html", context={"form": form, "board": board, "messages": messages})

"""

def boardbyuuid(request, board_uuid):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            newmessage = Message.objects.create(
                text=form.cleaned_data["text"]
                )
            newmessage.save()
            updatedboard = Board.objects.get(uuid=board_uuid)
            updatedboard.messages_uuids += f" {newmessage.uuid}"
            updatedboard.save()
            return render(request, "board.html")
        else:
            HttpResponse("dflj")

    else:
        board = Board.objects.get(uuid=board_uuid)
        messages = ""
        form = MessageForm()
        if board.messages_uuids != "":
            messages = Message.objects.filter(uuid__exact=board.messages_uuids)
            return render(request, "board.html", context={"board": board, "messages": messages, "form": form})

"""







