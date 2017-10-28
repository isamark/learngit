from django.shortcuts import render,get_object_or_404
from .models import Post,Tag,Category
from comments.models import Comment
# 引入markdown模块
import markdown
# 引用类视图
from django.views.generic import ListView


# 详情
def detail(request,post_id):
    post = get_object_or_404(Post,id = int(post_id))
    post.body = markdown.markdown(post.body,
                                  extensions = [
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    comment_all = Comment.objects.filter(post_id=post_id).order_by('-id')[:5]
    context = {'post':post,'comment_all':comment_all}
    return render(request,'blog/detail.html',context)


# 定义一个类，使其继承ＬistView
class IndexView(ListView):
    # 即将渲染的模板
    template_name = 'blog/index.html'
    # 指定获取的模型列表保存的变量名，遮盖变量会跟下面生成的context一同传递给模板
    context_object_name = 'post_all'
    # 指定每页显示的数据数量
    paginate_by = 1
    # 指明从哪个模型类获取数据
    def get_queryset(self):
        return Post.objects.order_by('-created_time')

    """
    在父类中有get_context_data()方法，在子类中重写该方法，
    同时为了在子类中使用父类中已经有的数据[paginator,page_obj,is_paginated]
    这是三个字典形式的模板变量，
    可以认为以上这三个数据是工厂的上游半成品，需要经过处理，再获取需要的产品
    然后又送回来，无论加工与否，出口都一样
    """

    def get_context_data(self, **kwargs):

        # 使用super()调用mro()列表中第一个父类的的get_context_data()方法
        # python3 super()不需要参数
        context = super().get_context_data()

        """
        paginator 是Paginator的一个实例，
        page_obj 是Page的一个实例，
        is_paginated 是一个布尔变量，用于指示是否已分页
        由于context是一个字典，所以调用get方法，从中取出某个键对应的值
        """
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        # 调用自己写的pagination_data()方法，获取显示分页导航条所需的数据
        pagination_data = self.pagination_data(paginator,page,is_paginated)

        # 将获取的分页导航条的模板变量更新到context中，注意pagination_data返回值也是一个字典
        context.update(pagination_data)

        # 将更新后的context返回，以便ListView使用字典中的模板变量取渲染模板
        # 这个时候context字典中已经有了显示分页的导航条所需的数据
        return context

    def pagination_data(self,paginator,page,is_paginated):
        if not is_paginated:
            # 如果没有分页，则无需分页导航条，不需要数据
            return {}

        # 当前页左边连续的页码号，初始值为空
        left = []

        # 当前页右边连续的页码号，初始值为空
        right = []

        # 标示第１页页码后是否需要显示省略号
        left_has_more = False

        # 标示最后一页前是否需要省略号
        right_has_more = False

        # 表示是否需要显示第一页
        # 因为如果当前页左边的连续页码中已经含有了第一页此时就不需要专门显示第一页了
        # 其他情况需要专门显示第一页
        # 默认值为Ｆalse
        first = False

        # 与上类似
        last = False

        page_number = page.number

        total_pages = paginator.num_pages

        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number + 2]

            if right[-1] < total_pages - 1:
                right_has_more = True

            if right[-1] < total_pages:
                last = True

        elif page_number == total_pages:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]

            if left[0] > 2:
                left_has_more = True

            if left[0] > 1:
                first = True

        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]

            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True

        data = {
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'first':first,
            'last':last,
        }

        return data


# 分类
# 继承IndexView类
class CategoryView(IndexView):

    # 仔细观察你会发现这里少了３行，继承了
    def get_queryset(self):
        category = get_object_or_404(Category,pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=category)


# 标签
class TagView(IndexView):

    def get_queryset(self):
        tag = get_object_or_404(Tag,pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(tags=tag)

