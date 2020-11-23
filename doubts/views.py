from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.db import IntegrityError

from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views.generic import DetailView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.contrib.auth.models import User, auth
from .models import Item
from .models import Question
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, date
from .forms import Askdoubt

# Create your views here.
@login_required
def homepage(request):
    obj =Item.objects.all()
    return render(request, 'doubts/home.html',{'obj' : obj})

def courses(request):
    obj =Item.objects.all()
    return render(request, "doubts/courses.html", {'obj' : obj})

#def video(request):
#    obj =Item.objects.all()
 #   return render(request, 'doubts/video.html',{'obj' : obj})
def askquestion(request):
    if request.user.is_authenticated:
        student_name = request.user
        if request.method == 'POST':
            form = Askdoubt(request.POST , request.FILES)
            if form.is_valid():
                coursename = form.cleaned_data.get('coursename')
                doubt = form.cleaned_data.get('doubt')
                Question.objects.create(
                    student_name = request.user,
                    coursename = coursename,
                    doubt = doubt,
                )
                return redirect('homepage')
        else:
            form = Askdoubt()
        return render(request, 'doubts/form.html', {'form':form})

