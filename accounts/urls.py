from django.urls import path
from .views import (
    change_password,
    forget_password,
    login,
    register,
    reset_password,
    user_profile,
    logout
)

urlpatterns = [
    path('change-password', change_password, name='change_password'),
    path('forget-password', forget_password, name='forget_password'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='register'),
    path('reset-password', reset_password, name='reset_password'),
    path('user-profile', user_profile, name='user_profile'),
]