# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.models import *
from api.serializers import MovieSerializer, ClientAccessTokenSerializer, CinemaSerializer


def index(request):
    return render_to_response('template.html')


@api_view(['GET', 'POST'])
def movie_list(request):
    """
    List all movies or create a new movie record.
    """
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def cinema_list(request):
    """
    List all cinemas or create a new cinema record.
    """
    if request.method == 'GET':
        cinemas = Cinema.objects.all()
        serializer = CinemaSerializer(cinemas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CinemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_token(request):
    data = request.data
    key = data.get('key')
    secret = data.get('secret')
    try:
        client = APIClient.objects.get(key=key, secret=secret)
        # iv, access_token, tag, client.expires_on = general.create_client_access_token(client.key, client.secret,
        # client.name)
    except Exception as err:
        raise serializers.ValidationError(str(err))

    serializer = ClientAccessTokenSerializer(client)
    return Response(serializer.data, status=status.HTTP_200_OK)


class GetClientAccessToken(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = ClientAccessTokenSerializer
