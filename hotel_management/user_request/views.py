#-------- Django Import--------#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

#-------- Model Import--------#
from .models import Service_Amenities_Request_Model,User_Food_Request,Washing_machine_request

#-------- Form Import-------#
from .forms import Food_Request_Form, Service_Amenities_Request_Form,Washing_machine_request_Form




# Create your views here.

#-------- Food Request View --------#
class FoodRequest(LoginRequiredMixin,View):


 def get(self, request):
  form = Food_Request_Form()
  return render(request, 'user_request/user_request_form.html', {'form':form})   


 def post(self, request,*args, **kwargs):
  form = Food_Request_Form(request.POST,request.FILES,)
  form.instance.user_request = request.user
  if form.is_valid():
   form.save()
   return render(request, 'user_request/user_request_form.html', {'form':form})

#-------- Service Amenities request View --------#
class Service_Amenities_Request(LoginRequiredMixin,View):


 def get(self, request):
  form = Service_Amenities_Request_Form()
  return render(request, 'user_request/Service_Amenities_Request_Form.html', {'form':form})   


 def post(self, request,*args, **kwargs):
  form = Service_Amenities_Request_Form(request.POST)
  form.instance.user_request = request.user
  if form.is_valid():
   form.save()
   return render(request, 'user_request/Service_Amenities_Request_Form.html', {'form':form})

#-------- Washing Machine request View --------#   

class Washing_machine_Request_View(LoginRequiredMixin,View):


 def get(self, request):
  form = Washing_machine_request_Form()
  return render(request, 'user_request/washing_machine_form.html', {'form':form})   


 def post(self, request,*args, **kwargs):
  form = Washing_machine_request_Form(request.POST)
  form.instance.user_request = request.user
  if form.is_valid():
   form.save()
   return render(request, 'user_request/washing_machine_form.html', {'form':form})



 

#-------- Service Amenities View To Show All The Request--------#
def show_request(request):
    context = {
        'service_request': Service_Amenities_Request_Model.objects.all()
    }
    return render(request, 'user_request/show_service_amenities_request.html', context)   

#-------- Request View To Show All The Food Request--------#
def show_food_request(request):
    context = {
        'Food_request': User_Food_Request.objects.all()
    }
    return render(request, 'user_request/food_request_show.html', context)  



#-------- Washing View To Show All The Washing Request--------#      

def show_washing_request(request):
    context = {
        'washing_machine': Washing_machine_request.objects.all()
    }
    return render(request, 'user_request/show_washing_request.html', context)  
