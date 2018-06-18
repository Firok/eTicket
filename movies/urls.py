# -*- coding: utf-8 -*-
from django.conf.urls import url
from movies import views
from django.conf import settings
from django.conf.urls.static import static


# Resources url
urlpatterns = [
    url(r'^$', views.index, name='movies-index'),
    url(r'^(?P<slug>[-\w]+)/$', views.movie_select_show, name='movie'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
