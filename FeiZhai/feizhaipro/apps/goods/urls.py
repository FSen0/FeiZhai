from django.urls import path
from apps.goods.views import *

app_name = 'goods'
urlpatterns = [
    path('homepage/',Goodshome.as_view(),name='goodshome'),
    path('toy/',Goodstoy.as_view(),name='goodstoy'),
    path('detail/',Goodsdet.as_view(),name='goodsdetail' ),
    path('cloths/',Goodscloths.as_view(),name='goodscloths')
]