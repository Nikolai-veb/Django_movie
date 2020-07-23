from rest_framework import serializers
from .models import Movie, Review, Rating


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтрацыя отзывов, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializers(serializers.ModelSerializer):
    """Вывод рекурсии chldren"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data



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

    children = RecursiveSerializers(many=True)


    class Meta:
        list_serialiser_class = FilterReviewListSerializer
        model = Review
        fields = ("name", "text", "children")


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


class RatingCreateSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""
    class Meta:
        model = Rating
        fields = ("star", "movie")


    def create(self, validated_data):
        ratings = Rating.objects.update_or_create(
            ip=validated_data.get("ip", None),
            movie=validated_data.get("movie", None),
            defaults={"star":validated_data.get("star")}
        )
        return ratings

