from django.urls import path
from django.conf.urls import url
from apps.user.views import *
from django.contrib.auth.decorators import login_required

app_name = 'user'
urlpatterns = [
    url(r'^$',showhome,name='homepage'),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('userinfo/',login_required(Userinfo.as_view()),name='userinfo'),
    path('delartcollect/<artid>/',Delartcollect.as_view(),name='delartcollect'),
    path('active/<token>/', ActiveView.as_view(), name='active')
]