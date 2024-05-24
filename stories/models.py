from django.db import models
from django.contrib.auth import get_user_model
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
    tags = models.ManyToManyField('Tag', related_name='receipes')

    def __str__(self) -> str:
        return self.title


class Category(TimeStamp):
    name = models.CharField('Name', max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField('Name', max_length=100)

    def __str__(self) -> str:
        return self.name
    