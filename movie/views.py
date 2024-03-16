from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from movie.models import Movie, Director, Review
from movie.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, MovieReviewSerializer, \
    MovieValidateSerializer


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        queryset = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(queryset)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = MovieValidateSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "DELETE":
        queryset.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == "GET":
        queryset = Director.objects.all()
        serializer = DirectorSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = DirectorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        queryset = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(queryset)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = DirectorSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "DELETE":
        queryset.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == "GET":
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        queryset = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(queryset)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movie_review_list_api_view(request):
    queryset = Movie.objects.all()
    serializer = MovieReviewSerializer(queryset, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class MovieReviewListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer
