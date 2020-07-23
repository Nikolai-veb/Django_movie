from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MovieListSerializers, MovieDetailSerializers, ReviewCreateSerializers, RatingCreateSerializer

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


class AddStarRatingView(APIView):
    """Добавление звезд рейтинга"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(' , ')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        serializer = RatingCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=self.get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)





class ReviewCreateView(APIView):
    """Добавление отзыва"""
    def post(self,request):
        reviews = ReviewCreateSerializers(data=request.data)
        if reviews.is_valid():
            reviews.save()
        return Response(status=201)
