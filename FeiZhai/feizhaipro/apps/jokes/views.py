from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import View
from apps.jokes.models import Joketype,Joke,Relationjokeuser

class Jokeshow(View):
    def get(self,request,type=1):
        cat=Joketype.objects.all()
        joke=Joke.objects.filter(joketype=type)
        return render(request,'jokeshow.html',locals())

class Collectjoke(View):
    def get(self,request,jokeid):
        userid=request.user.id
        jokeid=jokeid
        jokeuser=Relationjokeuser.objects.create(user_id=userid,joke_id=jokeid)
        jokeuser.save()
        return HttpResponseRedirect('/jokes/jokeshow/'+jokeid+'/')
