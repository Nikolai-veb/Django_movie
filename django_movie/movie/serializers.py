from rest_framework import serializers
from .models import Movie


class MovieListSerializers(serializers.ModelSerializer):
    """Серифлизатор Фильмов"""
    class Meta:

         model = Movie
         fields = ("title",
                  "tagline",
                  "category",
                  )




class MovieDetailSerializers(serializers.ModelSerializer):
    """Вывод фильмав"""
    category = serializers.SlugRelatedField(slug_field=name, read_only=True)
    directors = serializers.SlugRelatedField(slug_field=name, read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field=name, read_only=True, many=True)
    ganres = serializers.SlugRelatedField(slug_field=name, read_only=True, many=True)


    class Meta:

         model = Movie
         exclude = ("draft",)
