from django.shortcuts import render

from .models import Movie


class MoviesView(Views):

    def get(self, request):
        movie = Movie.objects.all()
        return render(request, 'movies/movie.html', {'movie_list':movie})

