from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Comment(models.Model):

    # 评论用户的名字
    name = models.CharField(max_length=100)

    # 用户发表的内容
    text = models.TextField()

    # 属于哪一篇博客的评论
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:10]
