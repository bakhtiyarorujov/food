from django.shortcuts import render, get_object_or_404
from .models import Receipe, Tag

# Create your views here.
def receipes(request):
   recipes = Receipe.objects.all().order_by('-created_at')
   context = {
      'recipes': recipes
   }
   return render(request, 'recipes.html', context=context)

def single_receipe(request, id):
   recipe = get_object_or_404(Receipe, id=id)
   tags = Tag.objects.all()
   context = {
      'recipe': recipe,
      'tags': tags
   }
   return render(request, 'single.html', context=context)

def stories(request):
   return render(request, 'stories.html')