from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (
    Receipe,
    Category,
    Tag,
    RecipeComment
)
# Register your models here.
# admin.site.register(Receipe)
# admin.site.register(Category)
# admin.site.register(Tag)
admin.site.register(RecipeComment)

@admin.register(Receipe)
class RecipeAdmin(TranslationAdmin):
    list_display = ['title', 'content', 'category', 'author']
    list_display_links = ['title', 'content', 'category', 'author']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    list_display = ['name']
    list_display_links = ['name']

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name']
    list_display_links = ['name']

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }