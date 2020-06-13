from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

    url(r"^$", views.MoviesView.as_view()),
    url("<slug:slug>", views.MovieDetailView.as_view(), name="movie_detail"),
    url("review/(?P<pk>\d+)$", views.AddReview.as_view(), name="add_review"),
]
