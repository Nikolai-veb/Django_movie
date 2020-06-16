from modeltranslation.translator import register, TranslationOptions
from .models import Category, Actor, Movie, Ganre, MovieShots



@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'discription')



@register(Actor)
class AktorTranslationOptions(TranslationOptions):
    fields = ('name', 'description')



@register(Ganre)
class GanreTranslationOptions(TranslationOptions):
    fields = ('name', 'discription')



@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline', 'description', 'country')


@register(MovieShots)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ('title', 'discriprion')
