#-------- Django Default Impor--------#
from django.contrib import admin
from django.urls import path

#-------- Room Management View Import--------#
from .views import Room_Management_View, Room_ManagementListView

#-------- URL Pattern--------#

urlpatterns = [

    path('availability/',Room_Management_View.as_view(),name='room-availability'),
    path('room_availability/',Room_ManagementListView.as_view(),name='room-list'),


]


