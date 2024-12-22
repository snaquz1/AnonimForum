from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.
def main(request):
    updates = Update.objects.all().order_by("-date")[:3]
    return render(request, "main.html", context={"updates": updates})

def updates(request):
    updates = Update.objects.all().order_by("-date")
    return render(request, "updates.html", context={"updates": updates})

def boards(request):
    boards = Board.objects.all().order_by("-creation_date")
    return render(request, "boards.html", context={"boards": boards})

def boardbyuuid(request, board_uuid):
    global board, messages
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(board=get_object_or_404(Board, uuid=board_uuid), text=form.cleaned_data["text"]).save()
            return HttpResponseRedirect(f"/boards/{board_uuid}")
        else:
            return HttpResponse(form.errors)
    else:
        form = MessageForm()
        board = Board.objects.get(uuid=board_uuid)
        messages = Message.objects.filter(board_id=board.id)
    return render(request, "board.html", context={"form": form, "board": board, "messages": messages})


def boardaction(request, action):
    if request.method == "POST" and action == "create":
        form = BoardCreationForm(request.POST, request.FILES)
        if form.is_valid():
            Board.objects.create(
                name=form.cleaned_data["name"],
                image=form.cleaned_data["image"]
            ).save()
            return redirect("/boards")

    else:
        if action == "create":
            form = BoardCreationForm()
            return render(request, "boardcreation.html", context={"form": form})
