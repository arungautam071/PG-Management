#-------- Django Form Import --------#
from django import forms

#-------- Model Import--------#
from .models import Room_Management

#--------Radio Button Input--------#

Room_Type = [
 ('Single', 'Single'),
 ('Double', 'Double'),
 ('Triple','Triple')
]
Room_Status=[
    ('Available','Available'),
    ('Not-Available','Not-Available')
]
Room_For=[
    ('Boy','Boy'),
    ('Girl','Girl')
]


#-------- Form Logic Room Management Form--------#

class Room_Management_Form(forms.ModelForm):
    room_type = forms.ChoiceField(choices=Room_Type, widget=forms.RadioSelect)
    room_status = forms.ChoiceField(choices=Room_Status, widget=forms.RadioSelect)
    room_for = forms.ChoiceField(choices=Room_For, widget=forms.RadioSelect)
    check_in_date = forms.DateField(required=False)
    class Meta:
        model=Room_Management
        fields=['room_number','room_type','room_status','room_for','check_in_date']
        