from django.shortcuts import render
from django.views.generic import View,CreateView,DetailView,DeleteView
from renter.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse
# Create your views here.
class home(View):
   def get(self,request):
      brands=Brand.objects.all()
      bikes=Bike.objects.all()
      un=request.session.get('username')
      if un:  
         UO=User.objects.get(username=un)
         d={'brands':brands,'bikes':bikes,'UO':UO}
         return render(request,'renter/home.html',d)
      d={'brands':brands,'bikes':bikes}
      return render(request,'renter/home.html',d)
      
   

class register(View):
   def get(self,request):
      ERFO=RenterForm()
      ERPFO=RProfileForm()
      d={'ERFO':ERFO,'ERPFO':ERPFO}
      return render(request,'renter/register.html',d)
   
   def post(self,request):
      if request.FILES:
         RFDO=RenterForm(request.POST)
         RPFDO=RProfileForm(request.POST,request.FILES)
         if RFDO.is_valid() and RPFDO.is_valid():
            pw=RFDO.cleaned_data.get('password')
            MRFDO=RFDO.save(commit=False)
            MRFDO.set_password(pw)
            MRFDO.is_staff=True
            MRFDO.save()
            MRPFDO=RPFDO.save(commit=False)
            MRPFDO.username=MRFDO
            MRPFDO.save()
            return HttpResponseRedirect(reverse('renter_login'))
         return HttpResponse('invalid data')

class renter_login(View):
   def get(self,request):
      return render(request,'renter/login.html')
   def post(self,request):
      un=request.POST.get('un')
      pw=request.POST.get('pw')
      ARO=authenticate(username=un,password=pw)
      if ARO and ARO.is_staff==True:
         login(request,ARO)
         request.session['username']=un
         return  HttpResponseRedirect(reverse('renter_home'))
      return HttpResponse('authenticated user not found')
      
class renter_logout(View):
   def post(self,request):
      logout(request)
      return HttpResponseRedirect(reverse('renter_login'))
   
class renter_profile(View):
    def post(self,request):
        un=request.session.get('username')
        RUO=User.objects.get(username=un)
        RPO=RenterProfile.objects.get(username=RUO)
        d={'RPO':RPO,'RUO':RUO}
        return render(request,'renter/profile.html',d)
  
class addbike(CreateView):
    model= Bike
    fields='__all__'
    success_url='addbike'  
  
            
class display(DetailView):
   model=Bike
   context_object_name='bike'

class bikedisplay(View):
    def get(self,request,brand):
        un=request.session.get('unsername')
        UO=User.objects.get(username=un)
        brands=Brand.objects.all()
        bikes=Bike.objects.filter(company=brand)
        d={'bikes':bikes,'brands':brands,'UO':UO}
        return render(request,'renter/home.html',d)
   
 
            
             
   
   