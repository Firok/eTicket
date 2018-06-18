# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from movies.models import Movie, Media


def index(request):
    movies = Movie.objects.all()
    medias = Media.objects.all()
    list = zip(movies, medias)
    return render_to_response('movies.html',
                              {'list': list})


def movie_select_show(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    return render_to_response('movie_select_show.html',
                              {'movie': movie, })
