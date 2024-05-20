from django.urls import path
from .views import home, about_us, contact

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about_us'),
    path('contact-us/', contact, name='contact_us')
]