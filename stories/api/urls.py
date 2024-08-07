from django.urls import path
from .views import categories, recipes, recipe_update, RecipeListView, RecipeRetriveUpdateDestroyView, TagListView


urlpatterns = [
    path('categories', categories, name='api_category_list'),
    path('tags', TagListView.as_view(), name='api_tag_list'),
    path('recipes', RecipeListView.as_view(), name='api_recipe_list'),
    path('recipe/<int:pk>', RecipeRetriveUpdateDestroyView.as_view(), name='api_recipe_update'),

]
