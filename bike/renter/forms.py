from django import forms
from .models import * 

class RenterForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email','username','password']
        help_texts={'username':' '}
        
class RProfileForm(forms.ModelForm)  :
    class Meta:
        model = RenterProfile
        exclude = ['username']   
