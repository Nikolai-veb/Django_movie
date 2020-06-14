from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

    url(r"^$", views.MoviesView.as_view()),
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    url("<slug:slug>", views.MovieDetailView.as_view(), name="movie_detail"),
    url("review/(?P<pk>\d+)$", views.AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail")
]
