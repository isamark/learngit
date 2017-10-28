from django.shortcuts import render
from django.shortcuts import redirect
from .models import CarInfo
from django.http import HttpResponse,JsonResponse
from df_user import user_decorator


@user_decorator.login
# 有两个地方会直接触发下面函数，直接点击购物车区域或者点击顶部的购物车
# 一个地方通过重定向触发
def cart(request):
    # 突然意识到一个问题，如果通过下面session方式获取你自己user_id，服务器不可能就你一个用户吧
    user_id = request.session['user_id']
    # 获取用户的所有购物车
    carts = CarInfo.objects.filter(user_id = user_id)
    context = {
        'carts':carts
    }

    return render(request,'df_cart/cart.html',context)

# 有两个地方可以触发这个函数 1:列表页商品上面的购物车　2:详情页加入购物车
@user_decorator.login
# 这个函数会传入两个参数，一个商品id和向购物车中添加几件该商品
def add(request,goods_id,count):
    # 向购物车添加数据，首先得获取用户
    user_id = request.session['user_id']
    # 然后也需要知道这是哪一件商品
    goods_id = int(goods_id)
    # 最后就是添加的数量
    count = int(count)
    # 获取一个购物车对象(filterl里面两个参数)
    cart_this = CarInfo.objects.filter(user_id = user_id,goods_id = goods_id)
    # 判断如果有该购物车，那么只需要改变该购物车对象的count字段就可以了
    if len(cart_this) >= 1:
        cart_this = cart_this[0]
        cart_this.count += count
    # 当然也有可能是第一次创建该购物车，则运行else里面的代码
    else:
        cart_this = CarInfo()
        cart_this.user_id = user_id
        cart_this.goods_id = goods_id
        cart_this.count = count
    # 仔细观察你会发现下面的一句代码，因为上面的if与else都需要保存
    cart_this.save()
    # 到此为止，已经把数据保存到数据库了
    # 下面要分道扬镳，如果是ajax请求，则就会返回count,并在购物车区域显示当前购物车数量
    if request.is_ajax():
        count = CarInfo.objects.filter(user_id = request.session['user_id']).count()
        # ajax返回，从哪里来，就从哪里回去
        return JsonResponse({'count':count})
    else:
        # 如果是从列表页进来，就需要重定向
        return redirect('/cart/')

# 在购物车页面与数据库交互的地方就是'去结算'与改变商品数量，还有删除购物车
# 而改变商品数量会改变数据库的数据，怎么样改变数据库的数据呢？下面这个函数为您揭晓
@user_decorator.login
def set_cart(request):
    # 这是一个ajax请求
    id = int(request.POST.get('id'))
    count1 = int(request.POST.get('count1'))
    c = CarInfo.objects.filter(id=id)[0]
    c.count = count1
    c.save()
    # 下面任何返回一个东西
    return HttpResponse(1)

# 这个是删除购物车运行的函数
def del_cart(request,cart_id):
    # 删除这一条数据
    CarInfo.objects.get(id=int(cart_id)).delete()
    # 下面这是一个暗号
    data = {'ok':1}
    # ajax返回data
    return JsonResponse(data)