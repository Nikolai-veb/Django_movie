from django.shortcuts import render
from django.views.generic.base import View

from .models import Movie


class MoviesView(View):

    def get(self, request):
        movie = Movie.objects.all()
        return render(request, 'movies/movie.html', {'movie_list':movie})

