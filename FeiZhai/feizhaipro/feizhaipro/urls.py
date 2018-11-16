
from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',include('apps.user.urls')),
    path('user/',include('apps.user.urls',namespace='user')),
    path('goods/',include('apps.goods.urls',namespace='goods')),
    path('imgshow/',include('apps.imgshow.urls',namespace='imgshow')),
    path('news/',include('apps.news.urls',namespace='news')),
    path('jokes/',include('apps.jokes.urls',namespace='jokes'))
]
