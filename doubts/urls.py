from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from doubts import views as user_views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import video

urlpatterns = [

path('index.html/', user_views.homepage, name="homepage"),
path('doubtsession/', user_views.askquestion, name="formpage"),
path('courses/', user_views.courses, name="courses"),
#path('video/', video)
]
