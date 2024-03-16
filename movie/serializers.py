from rest_framework import serializers
from .models import Director, Movie, Review, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count')

    @staticmethod
    def get_movies_count(obj):
        return obj.movies.count()


class MovieSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'tags')


class MovieValidateSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(write_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'tags')

    @staticmethod
    def validate_tags(value: list):
        for tag_id in value:
            try:
                Tag.objects.get(id=tag_id)
            except Tag.DoesNotExist:
                raise serializers.ValidationError(f'Тег с id {tag_id} не найден!')
        return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'movie', 'stars')


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    @staticmethod
    def get_average_rating(obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'reviews', 'average_rating')
