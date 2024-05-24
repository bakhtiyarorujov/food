from django.urls import path
from .views import receipes, single_receipe, stories

urlpatterns = [
    path('receipes', receipes, name='receipes'),
    path('single_receipe', single_receipe, name='single_receipe'),
    path('stories', stories, name='stories'),
]