from django.contrib import admin
from .models import *

from embed_video.admin import AdminVideoMixin
from .models import Item
from .models import Question

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
admin.site.register(Question)
