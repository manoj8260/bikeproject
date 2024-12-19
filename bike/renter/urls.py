from django.urls import path
from renter.views import * 
urlpatterns=[
    path('',home.as_view(),name='renter_home'),
    path('register/',register.as_view(),name='renter_register'),
    path('login/',renter_login.as_view(),name='renter_login'),
    path('logout/',renter_logout.as_view(),name='renter_logout'),
    path('profile/',renter_profile.as_view(),name='renter_profile'),
    path('addbike/',addbike.as_view(),name='addbike'),
    path('display<pk>',display.as_view(),name='rdisplay'),
    path('bikedisplay<brand>',bikedisplay.as_view(),name='bikedisplay'),
    
    
]