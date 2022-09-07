from django.contrib import admin

#-------- Model Import --------#
from .models import Profile,Contact_Form_Model

# Register your models here.
admin.site.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id','user']


@admin.register(Contact_Form_Model)
class Contact_Form_ModelModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'contact_number', 'subject', 'message']