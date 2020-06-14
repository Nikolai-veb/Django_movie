from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie, Actor
from .forms import ReviewForm

class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    


class MovieDetailView(DetailView):
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



class ActorView(DetailView):
    """Вывод детальнтй информацыи о актере"""
    model = Actor
    template_name = 'movie/actor.html'
    slug_fields = "name"
