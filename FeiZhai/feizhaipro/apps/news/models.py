from django.db import models
from base_m.base_model import BaseModel
from apps.user.models import User



class Articletype(models.Model):
    typename=models.CharField(max_length=20,verbose_name='文章类型')

    class Meta:
        db_table = 'fz_newstype'
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.typename

class Article(models.Model):
    arttitle=models.CharField(max_length=20,verbose_name='标题')
    artauthor=models.CharField(max_length=20,verbose_name='作者名称',null=True)
    artdesc = models.CharField(max_length=500, verbose_name="文章简介")
    artcontent = models.TextField(verbose_name="文章内容")
    artdate = models.CharField(max_length=50, verbose_name="发表时间",null=True)
    arttype = models.ForeignKey(Articletype, on_delete=models.CASCADE, verbose_name="文章类型")
    artimg =models.CharField(max_length=200,verbose_name='图片链接',null=True)
    user = models.ManyToManyField(User,through='Relationartuser',null=True)

    def __str__(self):
        return self.arttitle

    class Meta:
        db_table = 'fz_news'
        verbose_name = "文章"
        verbose_name_plural = verbose_name

class Comment(models.Model):
    comcontent=models.TextField()
    comuser=models.ForeignKey(User,on_delete=models.CASCADE)
    comart=models.ForeignKey(Article,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        db_table = 'fz_newscomment'
        verbose_name = "文章评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comcontent[:10]

class Relationartuser(models.Model):
    user=models.ForeignKey(User,on_delete=True)
    art=models.ForeignKey(Article,on_delete=True)

    class Meta:
        db_table = 'fz_artcollect'
        verbose_name = "文章收藏"
        verbose_name_plural = verbose_name