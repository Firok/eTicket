# -*- coding: utf-8 -*-
from django.conf.urls import url
from api import views
from django.conf import settings
from django.conf.urls.static import static


# Resources url
urlpatterns = [
    url(r'^movies/$', views.movie_list),
    url(r'^cinemas/$', views.cinema_list),
    url(r'^get/client/access/$', views.get_token),
    url(r'^$', views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
