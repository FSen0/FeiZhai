from django.urls import path
from apps.imgshow.views import *

app_name = 'imgshow'
urlpatterns = [
    path('imghomepage/',Imghomepage.as_view(),name='igmhomepage')
]