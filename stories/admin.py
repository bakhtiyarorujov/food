from django.contrib import admin
from .models import (
    Receipe,
    Category,
    Tag
)
# Register your models here.
admin.site.register(Receipe)
admin.site.register(Category)
admin.site.register(Tag)