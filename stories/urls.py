from django.urls import path
from .views import (
    single_receipe, 
    stories, 
    like_post,
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView
)

urlpatterns = [
    path('receipes', RecipeListView.as_view(), name='receipes'),
    path('liked/<int:id>', like_post, name='like'),
    path('recipe/<slug:slug>', RecipeDetailView.as_view(), name='single_receipe'),
    path('stories', stories, name='stories'),
    path('recipe/create', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/update/<int:pk>', RecipeUpdateView.as_view(), name='recipe_update')
]