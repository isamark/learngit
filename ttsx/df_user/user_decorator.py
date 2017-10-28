#coding = utf-8
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def login(func):
    def login_fun(request,*args,**kwargs):
        print(request)
        if request.session.has_key('user_id'):
            print(555555555555555555666666666666666666666666666666666666555555555555555555)
            return func(request,*args,**kwargs)

        else:
            print('奇怪了奇怪了奇怪了奇怪了奇怪了奇怪了奇怪了奇怪了奇怪了奇怪了奇怪了奇怪了奇怪了')
            red = HttpResponseRedirect('/user/login/')
            print(red)
            # red.set_cookie('url',request.get_full_path())
            request.session['url'] = request.get_full_path()
            print(request.session['url'])

            return red

    return login_fun