from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Receipe, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import CommenttForm, RecipeCreateForm
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def receipes(request):
#    print(f"Liked posts: {request.session.get('liked_posts')}")
#    recipes = Receipe.objects.all().order_by('-created_at')
#    context = {
#       'recipes': recipes
#    }
#    return render(request, 'recipes.html', context=context)


class RecipeListView(ListView):
   template_name = 'recipes.html'
   model = Receipe
   context_object_name = 'recipes'
   ordering = ['created_at']
   paginate_by = 3

   def get_queryset(self) -> QuerySet[Any]:
      queryset = super().get_queryset()
      cat_id = self.request.GET.get('category')
      tag_id = self.request.GET.get('tag')
      if cat_id:
         queryset = Receipe.objects.filter(category__id=cat_id)
      if tag_id:
         queryset = Receipe.objects.filter(tags__id=tag_id)
      return queryset

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


class RecipeDetailView(DetailView, FormMixin):
   template_name = 'single.html'
   model = Receipe
   context_object_name = 'recipe'
   form_class = CommenttForm

   def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
      context = super().get_context_data(**kwargs)
      context['tags'] = Tag.objects.all()
      return context

   def post(self, request, *args, **kwargs):
      self.object = self.get_object()
      form = self.get_form()
      if form.is_valid():
         return self.form_valid(form)
      else:
         return self.form_invalid(form)
   
   def form_valid(self, form):
       form.instance.recipe = self.object
       form.instance.user = self.request.user
       form.save()
       return super().form_valid(form)

   def get_success_url(self) -> str:
      return reverse_lazy('single_receipe', kwargs={'pk': self.object.pk})
   

def stories(request):
   return render(request, 'stories.html')


class RecipeCreateView(LoginRequiredMixin, CreateView):
   template_name = 'create_recipe.html'
   form_class = RecipeCreateForm
   # success_url = reverse_lazy('home')

   def form_valid(self, form):
       form.instance.author = self.request.user
       return super().form_valid(form)
   

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
   template_name = 'create_recipe.html'
   form_class = RecipeCreateForm
   model = Receipe
