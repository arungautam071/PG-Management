from platform import machine
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
# Create your models here.

class User_Food_Request(models.Model):
    user_request=models.ForeignKey(User,on_delete=models.CASCADE)
    request_date=models.DateTimeField(default=timezone.now)
    food_type_request=models.CharField(max_length=50)
    
    
class Service_Amenities_Request_Model(models.Model):
    user_request=models.ForeignKey(User,on_delete=models.CASCADE)
    request_date=models.DateTimeField(default=timezone.now)
    service_type_request=models.CharField(max_length=50)
    service_title=models.CharField(max_length=100)
    service_status=models.CharField(max_length=50)


#-------- Washing Machine Model --------#

class Washing_machine_request(models.Model):
    user_request=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile_number=models.IntegerField()
    put_in_time=models.DateTimeField(default=timezone.now)
    take_out_time=models.DateTimeField(default=timezone.now)
    machine_number=models.CharField(max_length=20)
    status=models.CharField(max_length=100)

