from django.db import models

# Create your models here.


class BookInfo(models.Model):
    """图书模型类"""
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    """英雄模型类"""
    hname = models.CharField(max_length=30)
    hgender = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=200)
    isDelete = models.BooleanField(default=False)
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE)


class AreaInfo(models.Model):
    """城市模块类"""
    title = models.CharField(max_length=30)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
