from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.views.generic import View
from apps.news.models import Article,Relationartuser,Comment

from apps.user.models import User
from django.core.paginator import Paginator

class Newspage(View):
    def get(self,request,arttype):
        art = Article.objects.filter(arttype=arttype)
        return render(request,'newspage.html',locals())

class Newsdetail(View):
    def get(self,request,artid):
        art=Article.objects.get(id=artid)
        com=Comment.objects.filter(comart_id=artid)
        return render(request,'newsdetail.html',locals())
    def post(self,request,artid):
        userid=request.user.id
        com=request.POST.get('comment-textarea')
        comm=Comment.objects.create(comuser_id=userid,comart_id=artid,comcontent=com)
        comm.save()
        return HttpResponseRedirect('/news/newsdetail/'+artid+'/')



class Newscollect(View):
    def get(self,request,artid):
        userid=request.user.id
        artid=artid
        artcot=Relationartuser.objects.create(user_id=userid,art_id=artid)
        artcot.save()
        return HttpResponseRedirect('/news/newspage/1/')



class Addart(View):
    def get(self,request):
        return render(request,'addart.html')
    def post(self,request):
        name = request.user.username
        title = request.POST.get('title')



