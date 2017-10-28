from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle

class GoodsInfo(models.Model):
    # 商品标题
    gtitle = models.CharField(max_length=20)
    # 商品图片 ImageField上传图片
    gpic = models.ImageField(upload_to='goods')
    # 商品价格 DecimalField表示十进制浮点数，max_digits表示几位数，decimal_places表示小数点后面是几位
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    # 商品的逻辑删除，并不是物理删除，BooleanField布尔值，默认不能为空
    isDelete = models.BooleanField(default=False)
    # 商品的单位 默认值为500g
    gunit = models.CharField(max_length=20,default='500g')
    # 商品的点击量 整型
    gclick = models.IntegerField()
    # 商品的简介
    gjianjie = models.CharField(max_length=200)
    # 商品的库存
    gkucun = models.IntegerField()
    # 商品的内容
    gcontent = HTMLField()
    # 商品的类型 通过外键与类TypeInfo关联
    gtype = models.ForeignKey(TypeInfo)

    def __str__(self):
        return self.gtitle




