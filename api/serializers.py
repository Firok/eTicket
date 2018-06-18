# -*- coding: utf-8 -*-
from rest_framework import serializers
from api.models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'synopsis', 'movie_type')


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('id', 'name', 'description')


class ClientAccessTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(allow_null=True, allow_blank=True)
    expires_on = serializers.DateTimeField(allow_null=True)
    expired = serializers.BooleanField(default=False)

    name = serializers.CharField()
    key = serializers.CharField()
    secret = serializers.CharField()
