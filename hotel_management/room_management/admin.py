from django.contrib import admin
from .models import Room_Management

# Register your models here.

#-------- Room Management admin page register--------#
@admin.register(Room_Management)
class Room_ManagementModelAdmin(admin.ModelAdmin):
    list_display = ['room_number','room_type','room_for','room_status','check_in_date']

