from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import OrderInfo,OrderDetailInfo
from datetime import datetime
from django.db import transaction
from df_cart.models import CarInfo
from df_user.models import UserInfo
from df_user import user_decorator


# 在购物车页面点击＂去结算＂触发下面函
def order(request):
    # 通过getlist获取选中的购物车的列表
    get = request.GET.getlist('cart_id')
    # 定义一个空列表
    cart_buy_all = []
    # 遍历get这个列表
    for cart_id in get:
        cart = CarInfo.objects.get(id=int(cart_id))
        # 给列表添加数据
        cart_buy_all.append(cart)
    # 请注意这里要把get也传进去，因为在个人订单那里需要更新数据库数据
    context = {
        'cart_buy_all':cart_buy_all,
        'get':get,
    }
    # 渲染
    return render(request,'df_order/order.html',context)

# 在订单页面点击提交订单后触发下面函数
@transaction.atomic()
def order_detail(request):
    # 首先设置一个点，可以随时回到这个回滚点
    tran_id = transaction.savepoint()
    # 获取刚才get的内容[想要的购物车的id]
    post = request.POST['cart_list_all']
    # 通过eval把字符串转化为列表
    post_change = eval(post)
    # 获取总价格
    ototal = request.POST['total_pay1']
    # 实例化一个订单
    order = OrderInfo()
    user_id = request.session.get('user_id')
    order.user_id = user_id
    order.oid = datetime.now().strftime('%Y%m%d%H%M%S') + str(user_id)
    order.odate = datetime.now()
    order.ototal = ototal
    order.save()

    # 订单详情
    # 首先遍历刚才的已经打算要的购物车里面的商品的id,并获得id所对应的购物车对象
    for id1 in post_change:
        #　实例化一个订单详情
        detail = OrderDetailInfo()
        #　此实例属于哪一个订单（一个订单里面有很多商品，一个商品对应一个购物车）
        detail.order = order
        #　判断商品的库存
        # {
        cart = CarInfo.objects.get(id=int(id1))
        goods = cart.goods
        #　如果库存大于购买数量
        if goods.gkucun >= cart.count:
            # 将真实的库存保存到数据库
            goods.gkucun = goods.gkucun - cart.count
            goods.save()
            # }
            detail.goods = goods
            detail.price = goods.gprice
            detail.count = cart.count
            detail.save()
            # 删除该购物车
            cart.delete()
        else:#如果库存小于购买数量
            transaction.savepoint_rollback(tran_id)
            return redirect('/cart/')
    transaction.savepoint_commit(tran_id)
    # 请注意这里是重定向，到订单详情页面
    return redirect('/user/user_center_order/')

# 在订单详情页面，点击去支付，会马上触发这个函数
def now_pay(request,order_oid):
    order = OrderInfo.objects.filter(oid=order_oid)[0]
    order.oIsPay = True
    order.save()
    return redirect('/user/user_center_order/')
