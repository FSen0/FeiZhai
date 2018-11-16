from django.shortcuts import render,redirect,HttpResponse,reverse
from django.views.generic import View
from apps.imgshow.models import Imgmain

class Imghomepage(View):
    def get(self,request):
        img=Imgmain.objects.all()
        return render(request,'imghomepage.html',locals())
