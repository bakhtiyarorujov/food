from django.urls import path
from .views import (
    receipes, 
    single_receipe, 
    stories, 
    like_post)

urlpatterns = [
    path('receipes', receipes, name='receipes'),
    path('liked/<int:id>', like_post, name='like'),
    path('recipe/<int:id>', single_receipe, name='single_receipe'),
    path('stories', stories, name='stories'),
]