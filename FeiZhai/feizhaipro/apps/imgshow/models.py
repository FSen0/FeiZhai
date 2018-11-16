from django.db import models
from base_m.base_model import BaseModel


class Imgmain(models.Model):
    '''图片展示首页'''
    imgname=models.CharField(max_length=50,verbose_name='图集名称')
    mainimg=models.ImageField(upload_to='imgmain',verbose_name='图集主图')
    imgtype=models.IntegerField(verbose_name='图片类型')
    class Meta:
        db_table = 'fz_imgmain'
        verbose_name = '图片主页'
        verbose_name_plural = verbose_name

class Imgdet(BaseModel):
    '''图片详情页'''
    mainimg=models.ForeignKey('Imgmain',verbose_name='图片详情',on_delete=True)
    imgname=models.CharField(max_length=50,verbose_name='图集名称')
    detimg=models.ImageField(upload_to='igmdet',verbose_name='图集详情图')

    class Meta:
        db_table = 'fz_imgdet'
        verbose_name = '图片详情页'
        verbose_name_plural = verbose_name
