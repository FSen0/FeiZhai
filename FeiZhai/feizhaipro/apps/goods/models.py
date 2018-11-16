from base_m.base_model import BaseModel
from django.db import models
from tinymce.models import HTMLField
from apps.user.models import User

class Goodstype(BaseModel):
    typename=models.CharField(max_length=50,verbose_name='商品分类')

    class Meta:
        db_table = 'fz_goodstype'
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

class Goodsmain(BaseModel):
    goodst = models.ForeignKey('Goodstype',verbose_name='商品属分类',on_delete=True)
    goodsname = models.CharField(max_length=50,verbose_name='商品名称')
    goodsmainimg = models.ImageField(upload_to='goodsmain')

    class Meta:
        db_table = 'fz_goodsmain'
        verbose_name = '主商品'
        verbose_name_plural = verbose_name

class Goodsdetail(models.Model):
    goodst = models.ForeignKey('Goodstype', verbose_name='商品属分类', on_delete=True)
    goodsname=models.CharField(max_length=50,verbose_name='商品名称')
    goodsprice=models.CharField(max_length=50,verbose_name='商品价格')
    goodscon=models.TextField(blank=True,verbose_name='商品简介')
    goodsimg=models.ImageField(upload_to='goodsdet')

    class Meta:
        db_table = 'fz_goodsdet'
        verbose_name = '商品详情'
        verbose_name_plural = verbose_name

# class Cart(BaseModel):
#     user=models.ForeignKey('User',verbose_name='购物车主人',on_delete=True)
#     goods=models.ForeignKey('Goodsmain',verbose_name='购物车商品',on_delete=True)
#
#     class Meta:
#         db_table = 'fz_cart'
#         verbose_name = '购物车'
#         verbose_name_plural = verbose_name