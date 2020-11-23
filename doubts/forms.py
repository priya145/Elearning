from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Question


class Askdoubt(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["coursename","doubt"]

    