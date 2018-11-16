from django.shortcuts import render,redirect,HttpResponse,reverse
from django.views.generic import View
from apps.goods.models import Goodsdetail

class Goodshome(View):
    def get(self,request):
        goods=Goodsdetail.objects.all()
        return render(request, 'goodhomepage.html',locals())

class Goodstoy(View):
    def get(self,request):
        toy = Goodsdetail.objects.filter(goodst_id=1)
        return render(request, 'goodtoy.html',locals())

class Goodscloths(View):
    def get(self,request):
        clo=Goodsdetail.objects.filter(goodst_id=2)
        return render(request, 'goodcloths.html',locals())

class Goodsdet(View):
    def get(self,request):
        good=Goodsdetail.objects.get(id=6)
        return render(request,'goodsdet.html',locals())