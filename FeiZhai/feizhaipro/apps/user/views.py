from django.shortcuts import render,redirect,HttpResponseRedirect,reverse,HttpResponse
from django.views.generic import View
from apps.user.models import User,Address
from django.contrib.auth import authenticate, login, logout
from apps.news.models import Article,Relationartuser
from apps.jokes.models import Joke,Relationjokeuser
from django.core.mail import send_mail
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from feizhaipro.settings import SECRET_KEY,EMAIL_FROM


def showhome(request):
    return render(request,'homepage.html')

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        rpwd = request.POST.get("repassword")
        email = request.POST.get("email")
        isactive=request.POST.get("is_active")

        if not all([username, pwd, rpwd, email]):
            return render(request, 'register.html', {'errmsg': '注册信息不完整'})
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user:
            return render(request, 'register.html', {'errmsg': '用户名以存在'})
        if pwd != rpwd:
            return render(request, 'register.html', {'errmsg': '两次密码输入不一致'})
        if isactive != 1:
            return render(request, 'register.html', {'errmsg': '请激活您的账户'})

        user = User.objects.create_user(username=username, email=email, password=pwd)
        user.save()

        serializer = Serializer(SECRET_KEY, 3600)
        info = {'confirm': user.id}
        token = serializer.dumps(info)
        token = token.decode()
        subject = '你好啊肥宅'
        message = '测试邮件！'
        sender = EMAIL_FROM
        receiver = [email]
        html_message = '<h1>%s, 欢迎您成为我的粉丝</h1>请点击下面链接激活您的账户<br/><a href="http://10.35.165.214:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (
            username, token, token)
        send_mail(subject, message, sender, receiver,html_message=html_message)

        return redirect(reverse('user:homepage'))

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                next_url = request.GET.get('next', reverse('user:homepage'))
                response = redirect(next_url)  # HttpResponseRedirect
                return response
            else:
                # 用户未激活
                return render(request, 'login.html', {'errmsg': '账户未激活'})
        else:
            # 用户名或密码错误
            return render(request, 'login.html', {'errmsg': '用户名或密码错误'})

class ActiveView(View):
    def get(self,request,token):
        serializer = Serializer(SECRET_KEY, 3600)
        try:  # 如果加密信息过期再进行解密会报错
            info = serializer.loads(token)
            user_id = info['confirm']  # 根据id获取用户并改变激活状态
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()
            return redirect(reverse('user:login'))  # 跳转到登录页面
        except SignatureExpired as e:

            return HttpResponse('激活链接已过期')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('user:homepage'))


class Userinfo(View):
    def get(self,request):
        userid=request.user.id
        artid=Relationartuser.objects.filter(user_id=userid)
        jokeid=Relationjokeuser.objects.filter(user_id=userid)
        cotart=[]
        for i in artid:
            a=Article.objects.get(id=i.art_id)
            cotart.append(a)
        cotjoke=[]
        for j in jokeid:
            a=Joke.objects.get(id=j.joke_id)
            cotjoke.append(a)
        return render(request,'userinfo.html',locals())

class Delartcollect(View):
    def get(self,request,artid):
        userid=request.user.id
        artid=artid
        a=Relationartuser.objects.filter(user_id=userid).filter(art_id=artid)
        a.delete()
        return HttpResponseRedirect('/user/userinfo/')