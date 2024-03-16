from django.urls import path

from movie import views
from movie.views import (
    DirectorListAPIView,
    DirectorDetailAPIView,
    MovieListAPIView,
    MovieDetailAPIView,
    ReviewListAPIView,
    ReviewDetailAPIView,
    MovieReviewListAPIView
)

# urlpatterns = [
#     path('directors/', views.director_list_api_view),
#     path('directors/<int:pk>/', views.director_detail_api_view),
#     path('movies/', views.movie_list_api_view),
#     path('movies/<int:pk>/', views.movie_detail_api_view),
#     path('reviews/', views.review_list_api_view),
#     path('reviews/<int:pk>/', views.review_detail_api_view),
#     path('movies/reviews/', views.movie_review_list_api_view)
# ]


urlpatterns = [
    path('directors/', DirectorListAPIView.as_view()),
    path('directors/<int:pk>/', DirectorDetailAPIView.as_view()),
    path('movies/', MovieListAPIView.as_view()),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view()),
    path('reviews/', ReviewListAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('movies/reviews/', MovieReviewListAPIView.as_view()),
]
