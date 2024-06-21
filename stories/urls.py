from django.urls import path
from .views import (
    single_receipe, 
    stories, 
    like_post,
    RecipeListView,
    RecipeDetailView
)

urlpatterns = [
    path('receipes', RecipeListView.as_view(), name='receipes'),
    path('liked/<int:id>', like_post, name='like'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='single_receipe'),
    path('stories', stories, name='stories'),
]