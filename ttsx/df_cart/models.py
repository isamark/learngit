# coding = utf-8
from django.db import models

# 谁买了几个什么
class CarInfo(models.Model):
    user = models.ForeignKey('df_user.UserInfo')
    goods = models.ForeignKey('goods.GoodsInfo')
    count = models.IntegerField()

    # def __str__(self):
    #     return self.user