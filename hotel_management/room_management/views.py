#-------- Django Import--------#
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

#-------- Form Import --------#
from .forms import Room_Management_Form

#-------- Django Generic Import--------#
from django.views.generic import (
    ListView,
)

#--------  Model Import --------#
from .models import Room_Management



#---------------- Class Based View's ----------------#

#-------- Room Management Form Logic--------#
class Room_Management_View(LoginRequiredMixin,View):
    def get(self, request):
        form = Room_Management_Form()
        return render(request, 'room_management/room_management_form.html',{'form':form})   

    def post(self, request,*args, **kwargs):
        form = Room_Management_Form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'room_management/room_management_form.html',{'form':form})

#-------- Room Management List View--------#
class Room_ManagementListView(ListView):
    model = Room_Management
    context_object_name = 'room_availability'
    template_name = 'room_management/room_availability.html'

    def get_queryset(self):
        return Room_Management.objects.filter().order_by('room_number')



