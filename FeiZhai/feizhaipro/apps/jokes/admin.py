from django.contrib import admin
from apps.jokes.models import *

# Register your models here.
admin.site.register([Joketype,Joke])