from django.contrib import admin
from apps.news.models import *
# Register your models here.

admin.site.register([Articletype,Article,Comment])