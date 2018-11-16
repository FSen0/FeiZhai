from django.urls import path
from apps.news.views import *
from django.contrib.auth.decorators import login_required

app_name = 'news'
urlpatterns = [
    path('newspage/<arttype>/',Newspage.as_view(),name='newspage'),
    path('newsdetail/<artid>/',Newsdetail.as_view(),name='newsdetail'),
    path('newscollect/<artid>/',Newscollect.as_view(),name='collect'),
    path('addart/',Addart.as_view(),name='addart'),
]