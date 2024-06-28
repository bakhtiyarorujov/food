from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
# Create your models here.
User = get_user_model()


class TimeStamp(models.Model):
    created_at = models.DateTimeField('Created Date', auto_now_add=True)
    updated_at = models.DateTimeField('Updated Date', auto_now=True)

    class Meta:
        abstract=True


class Receipe(TimeStamp):
    title = models.CharField('Title', max_length=200)
    content = models.TextField('Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receipes')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='receipes')
    cover = models.ImageField(upload_to='recipe_cover', null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='receipes')
    slug = models.SlugField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("single_receipe", kwargs={"slug": self.slug})
    
    def author_name(self):
        return self.author.get_full_name()

    class Meta:
        ordering = ['-created_at']


class RecipeComment(TimeStamp):
    recipe = models.ForeignKey(Receipe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user} {self.recipe}'


class Category(TimeStamp):
    name = models.CharField('Name', max_length=100)
    cover = models.ImageField(upload_to='category_cover', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField('Name', max_length=100)

    def __str__(self) -> str:
        return self.name
    