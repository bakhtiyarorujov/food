from django.urls import path
from .views import (
    home, 
    about_us, 
    ContactCreateView
) 

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about_us'),
    path('contact-us/', ContactCreateView.as_view(), name='contact_us')
]