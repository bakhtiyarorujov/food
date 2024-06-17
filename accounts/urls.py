from django.urls import path, re_path
from .views import (
    change_password,
    forget_password,
    login,
    register,
    reset_password,
    user_profile,
    logout,
    activate
)

urlpatterns = [
    path('change-password', change_password, name='change_password'),
    path('forget-password', forget_password, name='forget_password'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='register'),
    path('reset-password', reset_password, name='reset_password'),
    path('user-profile', user_profile, name='user_profile'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,35})/$',
    activate, name='activate'),
]