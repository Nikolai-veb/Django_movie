from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie, Actor, Category, Ganre
from .forms import ReviewForm


class GanreYear:
    """Жанры и года выхода Фильмов"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MoviesView(GanreYear, ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    


class MovieDetailView(GanreYear, DetailView):
    model = Movie
    slug_field = 'url'


class AddReview(View):
    """Отзовы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if  request.POST.get("parent",None):
                form.parent_id =init(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())



class ActorView(GanreYear, DetailView):
    """Вывод детальнтй информацыи о актере"""
    model = Actor
    template_name = 'movie/actor.html'
    slug_fields = "name"


class FilterMoviesView(GanreYear, ListView):
    """Фильтр фильмов"""
    def get_queryset(self):
        queryset = Movie.objects.filter(Q(year__in=self.request.GET.getlist("year"))|Q(genres__in=self.request.GET.getlist("genre")))
        return queryset


