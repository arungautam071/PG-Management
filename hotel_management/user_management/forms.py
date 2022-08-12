
#-------- Django Import--------#
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

#-------- Model And Form Import--------#

from .models import Profile

#-------- Form Logic For registration--------#

#-------- Register Form--------#
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model =User
        fields=['username','email','password1','password2']
        

#-------- Update Form --------#
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#--------Profile Update Form--------#
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','user_room_number']



     