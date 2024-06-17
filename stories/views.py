from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Receipe, Tag

# Create your views here.
def receipes(request):
   print(f"Liked posts: {request.session.get('liked_posts')}")
   recipes = Receipe.objects.all().order_by('-created_at')
   context = {
      'recipes': recipes
   }
   return render(request, 'recipes.html', context=context)

def like_post(request, id):
   # request.session['liked_posts'] = request.session.get('liked_posts', '') + str(id) + ' '
   # return render(request, 'recipes.html')
   response = HttpResponse('test')
   response.set_cookie('liked_posts', request.COOKIES.get('liked_posts', '') + str(id) + ' ')
   return response

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

