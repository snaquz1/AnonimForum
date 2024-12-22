from django import forms
from .models import Board

class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

class BoardCreationForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["name", "image"]
