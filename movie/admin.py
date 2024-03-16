from django.contrib import admin

from movie.models import Movie, Director, Review, Tag


class MovieAdmin(admin.ModelAdmin):
    list_per_page = 1


admin.site.register(Movie, MovieAdmin)
admin.site.register(Director)
admin.site.register(Review)
admin.site.register(Tag)
