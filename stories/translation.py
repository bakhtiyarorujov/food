from modeltranslation.translator import TranslationOptions,register
from .models import Receipe, Category, Tag

@register(Receipe)
class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)