from django import template
from blog.models import *
from doodle.models import *

register = template.Library()

@register.filter(name="deparenthesize")
def deparenthesize(value):
    return value.replace('"', '')



@register.inclusion_tag('blog/categories.html')
def blog_categories():
    return {
        'categories': Category.objects.all()
    }


@register.simple_tag
def user_to_project():
    return 

@register.simple_tag
def doodle_url():
    return Doodle.objects.latest('id').slika

@register.simple_tag
def doodle_avtor():
    return Doodle.objects.latest('id').avtor
