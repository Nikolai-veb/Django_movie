from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MovieListSerializers, MovieDetailSerializers, ReviewCreateSerializers

from .models import Movie, Actor, Category, Ganre
from django.urls import reverse



class MovieListView(APIView):
    """Вывод списка фильмов"""
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerializers(movies, many=True)
        return Response(serializer.data)



class MovieDetailView(APIView):
    """Вывод фильма"""
    def get(self, pk,  request):
        movies = Movie.objects.get(draft=False, id=pk)
        serializer = MovieDetailSeris(movies)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    """Добавление отзыва"""
    def post(self,request):
        reviews = ReviewCreateSerializers(data=request.data)
        if reviews.is_valid():
            reviews.save()
        return Response(status=201)
