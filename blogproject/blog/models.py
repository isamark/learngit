from django.db import models
from django.contrib.auth.models import User


# 分类
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 文章
class Post(models.Model):

    # 文章标题
    title = models.CharField(max_length=70)

    # 配图
    pic = models.ImageField(upload_to='blog')

    # 文章正文
    body = models.TextField()

    # 创建时间
    created_time = models.DateTimeField()

    # 创建地址
    address = models.CharField(max_length=20)

    # 哪个作者
    author = models.ForeignKey(User)

    # 点赞数量
    like = models.IntegerField()

    # 不喜欢数量
    nolike = models.IntegerField()

    # 简介
    excerpt = models.CharField(max_length=200,blank=True)

    # 属于哪个分类
    category = models.ForeignKey(Category)

    # 属于什么标签
    tags = models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return self.title





