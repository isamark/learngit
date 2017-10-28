from django import template
from ..models import Post,Category,Tag


register = template.Library()


# 最新文章模板标签
# @register.simple_tag
# def get_recent_posts(num = 5):
#     return Post.objects.all().order_by('-created_time')[:num]

# 分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def get_tags():
    return Tag.objects.all()