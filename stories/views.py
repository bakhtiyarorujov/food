from django.shortcuts import render
from .models import Receipe

# Create your views here.
def receipes(request):
   recipes = Receipe.objects.all()
   context = {
      'recipes': recipes
   }
   return render(request, 'recipes.html', context=context)

def single_receipe(request):
   return render(request, 'single.html')

def stories(request):
   return render(request, 'stories.html')