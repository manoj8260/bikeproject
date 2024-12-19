from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RenterProfile(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    phno=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to='renter_profile/')
    gender=models.CharField(max_length=20)

    def __str__(self) :
        return self.username.username

class Brand(models.Model):
    company=models.CharField(max_length=50,primary_key=True)
    branda_photo=models.ImageField(upload_to='branda_photo/')


    def __str__(self) :
        return self.company
    
class Bike(models.Model):
    company=models.ForeignKey(Brand,on_delete=models.CASCADE)
    bike_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    price=models.IntegerField(default=0)
    photo = models.ImageField(upload_to='bike_photos')
    ratting=models.FloatField(default=0.0)
    
    def __str__(self) :
        return self.bike_name
class Booking(models.Model):
    booking_id=models.IntegerField(primary_key=True)
    bike_name=models.ForeignKey(Bike,on_delete=models.CASCADE)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    pickup_date=models.DateField(auto_now=False,auto_now_add=False)
    pickup_time=models.TimeField(auto_now=False,auto_now_add=False)
    drop_date=models.DateField(auto_now=False,auto_now_add=False)
    drop_time=models.TimeField(auto_now=False,auto_now_add=False)

    def __str__(self) :
        return f" {self.username.username} {self.bike_name.bike_name} booking id is :  { str(self.booking_id) }"
    

