from django.db import models
from base_m.base_model import BaseModel
from apps.user.models import User

class Joketype(BaseModel):
    typename=models.CharField(max_length=20,verbose_name='笑话分类')

    class Meta:
        db_table = 'fz_joketype'
        verbose_name = '笑话分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.typename

class Joke(models.Model):
    joketype=models.ForeignKey('Joketype',verbose_name='分类',on_delete=True)
    jokecontent=models.CharField(max_length=5000,verbose_name='笑话内容')
    jokeauthor=models.CharField(max_length=50,verbose_name='作者名称')
    jokeimg=models.ImageField(upload_to='jokeimg',verbose_name='笑话图片',null=True)
    user=models.ManyToManyField(User,through='Relationjokeuser',null=True)
    class Meta:
        db_table = 'fz_joke'
        verbose_name = '笑话'
        verbose_name_plural = verbose_name

class Relationjokeuser(models.Model):
    user=models.ForeignKey(User,on_delete=True)
    joke=models.ForeignKey(Joke,on_delete=True)

