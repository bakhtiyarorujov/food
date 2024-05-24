from django.shortcuts import render

# Create your views here.
def receipes(request):
   return render(request, 'recipes.html')

def single_receipe(request):
   return render(request, 'single.html')

def stories(request):
   return render(request, 'stories.html')