from django import template
from movie.models import Category, Movie


register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.inclusion_tag('movie/tags/last_movie.html')
def get_last_movies(count=5):
    movies =Movie.objacts.order_dy("id")[:count]
    return {"last_movies" : movies}
