from rest_framework import serializers
from .models import Movie, Review


class MovieListSerializers(serializers.ModelSerializer):
    """Вывод списков фильмов"""
    class Meta:

         model = Movie
         fields = ("title",
                  "tagline",
                  "category",
                  )


class ReviewCreateSerializers(serializers.ModelSerializer):
    """Добавление отзывов"""
    class Meta:

         model = Review
         fields = ("__all__")



class ReviewSerializers(serializers.ModelSerializer):
    """Вывод отзывов"""
    class Meta:

         model = Review
         fields = ("name", "text", "parent")


class MovieDetailSerializers(serializers.ModelSerializer):
    """Вывод фильмав"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    ganres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    reviews = ReviewCreateSerializers(many=True)


    class Meta:

         model = Movie
         exclude = ("draft",)
