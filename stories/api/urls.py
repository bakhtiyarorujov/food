from django.urls import path
from .views import categories, recipes


urlpatterns = [
    path('categories', categories, name='api_category_list'),
    path('recipes', recipes, name='api_recipe_list'),
]
