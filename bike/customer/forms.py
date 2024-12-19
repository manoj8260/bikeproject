from django import forms
from customer.models import *
from renter.models import *
class CustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email','username','password']
        help_texts={'username':' '}



class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model= CustomerProfile
        exclude=['username']


class DateInput(forms.DateInput):
    input_type='date'

class TimeInput(forms.TimeInput):
    input_type='time'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude=['bike_name','username','booking_id']
        widgets={'pickup_date':DateInput(),'pickup_time':TimeInput(),'drop_date':DateInput(),'drop_time':TimeInput()}
