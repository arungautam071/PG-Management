from django.contrib import admin

#-------- Model Import --------#
from .models import Profile,Contact_Form_Model

# Register your models here.
@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','mobile_number','date_of_joining','id_proof_document','monthly_rent','security_amount']


@admin.register(Contact_Form_Model)
class Contact_Form_ModelModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'contact_number', 'subject', 'message']