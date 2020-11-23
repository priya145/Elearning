from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from landingpage.models import Profile
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.utils import timezone


class Question(models.Model):
    student_name=models.ForeignKey(User, on_delete=models.CASCADE, blank=True , null=True)
    coursename=models.CharField(max_length=100,blank=True,default =True)
    #blog=models.TextField(max_length=1000,blank=True)
    doubt=RichTextField(blank=True,null = False,default =True)
    date = models.DateField(auto_now_add=True,auto_now=False)
    

    def __str__(self):
        return self.student_name.username




class Item(models.Model):
    name = models.CharField(max_length=100,blank=True)
    video = EmbedVideoField()
    
    def __str__(self):
        return self.name
 
