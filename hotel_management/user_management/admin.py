from django.contrib import admin

#-------- Model Import --------#
from .models import Profile

# Register your models here.
admin.site.register(Profile)
