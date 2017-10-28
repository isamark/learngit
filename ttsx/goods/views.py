from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from goods.models import TypeInfo,GoodsInfo
from df_cart.models import CarInfo


# 运行下面函数会进入商场首页
def index(request):

    # 现获取所有生鲜类型的对象
    # 再获取每个类型对象的前四个商品对象
    type0 = TypeInfo.objects.all()[0]
    type0_fresh = type0.goodsinfo_set.all()[:4]

    type1 = TypeInfo.objects.all()[1]
    type1_fresh = type1.goodsinfo_set.all()[:4]

    type2 = TypeInfo.objects.all()[2]
    type2_fresh = type2.goodsinfo_set.all()[:4]

    type3 = TypeInfo.objects.all()[3]
    type3_fresh = type3.goodsinfo_set.all()[:4]

    type4 = TypeInfo.objects.all()[4]
    type4_fresh = type4.goodsinfo_set.all()[:4]

    type5 = TypeInfo.objects.all()[5]
    type5_fresh = type5.goodsinfo_set.all()[:4]

    # 为什么要用try? 因为获取首页并不需要登录，如果登录了，就需要获取购物车信息
    try:
        user_id = request.session['user_id']
    except KeyError:
        user_cart_count = 0
    else:
        # CarInfo.objects.filter()是一个QuerySet对象，有一个count()方法
        user_cart_count = CarInfo.objects.filter(user_id = user_id).count()

    context = {
        'type0':type0,'type1':type1,'type2':type2,
        'type3':type3,'type4':type4,'type5':type5,
        'type0_fresh':type0_fresh,'type1_fresh':type1_fresh,
        'type2_fresh':type2_fresh,'type3_fresh': type3_fresh,
        'type4_fresh':type4_fresh,'type5_fresh': type5_fresh,
        'user_cart_count':user_cart_count,
    }
    return render(request,'goods/index.html',context)


# 点击任意商品进入商品详情页面，触发下面函数
def detail(request,goods_id):

    # 获取urls匹配的那个id的商品对象,这里应用快捷函数get_object_or_404
    goods_this = get_object_or_404(GoodsInfo,pk = int(goods_id))
    # 能运行这个函数说明用户点击了该商品
    goods_this.gclick += 1
    goods_this.save()
    # 下面用try跟在首页作用一样
    try:
        user_id = request.session['user_id']
    except KeyError:
        user_cart_count = 0
    else:
        user_cart_count = CarInfo.objects.filter(user_id = user_id).count()
    # 新品推荐，从表查主表
    typeinfo_2 = GoodsInfo.objects.filter(gtype_id = goods_this.gtype.id).order_by('-id')[:2]
    res = render(request,'goods/detail.html',{'goods_this':goods_this,
                                               'user_cart_count':user_cart_count,
                                              'typeinfo_2':typeinfo_2
                                              })
    # 下面代码为了记录最近浏览的前五件商品，打印结果格式为:1,5,2,3,22
    goods_ids = request.COOKIES.get('goods_ids','')
    # 请注意这里的goods_id是字符串类型
    id = goods_id
    # 下面分类讨论goods_ids是有值还是空字符串
    if goods_ids != '':
        # 先把字符串拆成列表，每个元素都是字符串
        ids_list = goods_ids.split(',')
        # 然后判断goods_id是否在列表中，在则删除，然后把goods_id插入列表的第一个位置
        if id in ids_list:
            ids_list.remove(id)
        ids_list.insert(0,id)
        # 再判断列表长度是否等于６，等于则取前五个
        if len(ids_list) == 6:
            ids_list = ids_list[:5]
        # 然后拼接成字符串
        goods_ids = ','.join(ids_list)
        # 存入cookie
        res.set_cookie('goods_ids',goods_ids)
    # 如果是''，那么直接把goods_id存入cookie
    else:
        goods_ids = id
        res.set_cookie('goods_ids',goods_ids)
    # 对于下面的return其实上面这么一大坨就是个小小的插曲，这种设计还是挺有趣的
    return res


# 点击查看更多运行下面函数，进入列表页
# 把分页暂时删掉了，过几天加上
def list(request,tid,sort):
    type1 = get_object_or_404(TypeInfo,id=int(tid))
    try:
        user_id = request.session['user_id']
    except KeyError:
        user_cart_count = 0
    else:
        user_cart_count = CarInfo.objects.filter(user_id = user_id).count()
    if sort == '1':
        typeinfo_this = TypeInfo.objects.filter(id=tid)[0].goodsinfo_set.all().order_by('-id')
    elif sort == '2':
        typeinfo_this = TypeInfo.objects.filter(id=tid)[0].goodsinfo_set.all().order_by('gprice')
    elif sort == '3':
        typeinfo_this = TypeInfo.objects.filter(id=tid)[0].goodsinfo_set.all().order_by('-gclick')
    # 自己引发一个Http404异常
    else:
        raise Http404('找不到页面')


    return render(request,'goods/list.html',{
        'typeinfo_this':typeinfo_this,
        'type1':type1,
        'user_cart_count': user_cart_count

    })
