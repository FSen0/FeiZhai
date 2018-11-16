from django.urls import path
from apps.jokes.views import *

app_name = 'jokes'
urlpatterns = [
    path('jokeshow/<type>/',Jokeshow.as_view(),name='jokeshow'),
    path('collectjoke/<jokeid>/',Collectjoke.as_view(),name='jokecollect')
]