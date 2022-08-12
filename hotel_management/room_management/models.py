from django.db import models

# Create your models here.


#-------- Room Management model--------#

class Room_Management(models.Model):
    room_number=models.IntegerField()
    room_type=models.CharField(max_length=50)
    room_status=models.CharField(max_length=50)
    check_in_date=models.DateField(null=True)
    room_for=models.CharField(max_length=50)
                        
