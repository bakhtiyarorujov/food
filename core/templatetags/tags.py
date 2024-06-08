from django.template import Library
from stories.models import Category


register = Library()


@register.simple_tag
def get_categories(limit=5):
    return Category.objects.all()[:limit]