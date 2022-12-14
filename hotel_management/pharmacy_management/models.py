
#-------- Django Import --------
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#-------- Pharmacy Management Model --------#

class pharmacy_model(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE) 
    request_time=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=80,default="processing")
    prescription=models.ImageField(blank=True,upload_to='prescription_pics')
    billing_amount=models.IntegerField(default="0")
