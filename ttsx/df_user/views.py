#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from .models import *
from hashlib import sha1
from django.http import JsonResponse
import django
from goods.models import GoodsInfo
from df_user import user_decorator
from df_order.models import OrderDetailInfo,OrderInfo

#进入注册页面,输入ip后出发回车触发
def index(request):
    print(request.GET)
    # web应用的交互过程就是HTTP请求与响应的过程，打印request，我们会发现request就是一个实例化对象
    # 什么样的实例化对象呢？
    # 内容为：＂/user/register/＂,也就是把127.0.0.1:8000后面的内容制作成一个WSGIRequest对象(WSGIRequest继承http.HttpRequest)
    # 如何制作的呢？看django源代码
    # print(request,type(request))
    # <WSGIRequest: GET '/user/register/'> <class 'django.core.handlers.wsgi.WSGIRequest'>
    # print(isinstance(request,django.core.handlers.wsgi.WSGIRequest))
    # __bases__ 检测该类继承了哪个类，最后一定会追溯到object类
    # print(django.core.handlers.wsgi.WSGIRequest.__bases__)
    # print(HttpRequest.__bases__)
    # __mro__ 你所定义的任何一个类，python会计算出一个＂MRO 列表＂,该魔术方法就是查看这个列表
    # print(request,django.core.handlers.wsgi.WSGIRequest.__mro__)
    # print(isinstance(request,object))
    # 下面是render()方法,这个方法可神奇了,有六个参数， 其中有两个必须参数(request,template_name)
    return render(request,'df_user/register.html')

#判断账号是否被注册,失去焦点时触发
def register_exist(request):
    # ?uname='+$('#user_name').val()通过get的方式传参数
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    print(count)
    return JsonResponse({'count':count})

#如果账号没有被注册,则开始处理用户注册信息,提交后进入登录界面,点击注册后触发
def register_handle(request):
    uname = request.POST['user_name']
    upwd = request.POST['pwd']
    upwd2 = request.POST['cpwd']
    umail = request.POST['email']
    #判断两次输入的密码是否一致,不一致则进入注册页面
    if upwd != upwd2:
        return redirect('/user/register/')
    #对提交的密码加密,upwd3是加密后的密码
    s1 = sha1()
    s1.update(upwd.encode("gb2312"))
    upwd3 = s1.hexdigest()
    #创建UserInfo的实例化对象user,每一个用户的注册过程本质上讲都是一次实例化对象的过程
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.umail = umail
    user.save()
    # 这里采用重定向直接运行下面的函数
    return redirect('/user/login/')

#进入登录界面,重定向直接触发
def login(request):
    #request是WSGIRequest类的一个对象,COOKIES是WSGIRequest的一个方法,get是什么?
    #如果uname被存入cookie，则这里直接使用第一个参数uname,如果没有则为第二个参数
    #context参数'error_name','error_pwd'可以不填
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)

#填完数据进行处理,正常情况下，进入商场首页,点击登录后出触发
def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu',0)
    users = UserInfo.objects.filter(uname=uname)
    #判断数据库是否有当前用户名,没有则进入else直接输出“用户名错误”
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode("gb2312"))
        #用户名正确的情况下，判断密码是否正确，不正确则进入else，输出“用户名错误”
        #正确且选择了“记住”,则用户名存入cookie,
        if s1.hexdigest() == users[0].upwd:
            url = request.session.get('url','/goods/')
            red = HttpResponseRedirect(url)
            if jizhu != 0:
                # 因为HttpResponseRedirect继承于HttpResponse，set_cookie()是HttpResponse的方法，
                # 所以set_cookie可以被HttpResponseRedirect的对象red调用
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            #将id与用户名存入数据库中的session表
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red

        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1}
            return render(request, 'df_user/login.html', context)

    else:
        context = {'title':'用户登录','error_name':1,'error_pwd':0}
        return render(request,'df_user/login.html',context)

def logout(request):
    request.session.flush()
    return redirect('/goods/')

#点击个人信息
@user_decorator.login
def user_center_info(request):
    user_mail = UserInfo.objects.get(id=request.session['user_id']).umail
    # 下面为获取浏览记录
    # 获取到的结果为一个字符串如:'2,4,5,6,7'或者''
    goods_ids = request.COOKIES.get('goods_ids','')
    # 将上面的字符串以','拆分为列表，结果为:['2','4','5','6','7']或者['']
    goods_ids1 = goods_ids.split(',')
    goods_list = []
    # 没有浏览记录的时候goods_ids1为['']
    if goods_ids1 != ['']:
        for goods_id in goods_ids1:
            goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))
    context = {
        # 'title':'用户中心',
        'user_mail': user_mail,
        'user_name': request.session['user_name'],
        'goods_list': goods_list
    }
    return render(request,'df_user/user_center_info.html',context)

#点击全部订单
@user_decorator.login
def user_center_order(request):
    user_id = request.session['user_id']
    order = OrderInfo.objects.filter(user_id=user_id).order_by('-odate')
    return render(request,'df_user/user_center_order.html',{'order':order})

#点击送货地址
@user_decorator.login
def user_center_site(request):
    # 通过session获取一个对象（此对象为一个人的信息）,默认会显示用户为收件人
    user = UserInfo.objects.get(id=request.session['user_id'])
    return render(request,'df_user/user_center_site.html',{'user':user})

#添加收货人信息，可以改变默认收件人,填完收货地址，点击提交后触发
@user_decorator.login
def user_center_site_add(request):
    post = request.POST
    receiver = post.get('name')
    adress = post.get('adress')
    postcode = post.get('postcode')
    phone = post.get('phone')
    # 将填的收件人信息存入数据库,
    user = UserInfo.objects.get(id=request.session['user_id'])
    user.ureceiver = receiver
    user.uadress = adress
    user.upostcode = postcode
    user.uphone = phone
    user.save()
    return render(request,'df_user/user_center_site.html',{'user':user})
