#参考资料：
    # 李文周：迭代器和生成器入门
#从可迭代对象说起吧;
    #容器就是一个可以装东西的器皿，也是一种数据类型
    #可迭代对象就是一个容器，说白了就是一种对象，一种可以迭代的对象，属于Iterable类的实例化对象
    #Iterable类中有一个方法是“__iter__”,调用他会得到一个迭代器
    #常见的几种可迭代对象：str,list,touple,dict,set,打开的文件


from collections import Iterable,Iterator

#这就是一个str类的实例化对象
# str1 = 'I love you'
# print(isinstance(str1,Iterable))
# #对象调用类里的方法（或者iter(str1)）
# diedai = str1.__iter__()
# print(isinstance(diedai,Iterator))
# print(next(diedai))

#这就是一个list类的实例化对象
# list1 = [1,2,3,4,5,6,7,8,]
# print(isinstance(list1,Iterable))
# #对象调用类里的方法（或者iter(str1)）
# diedai = list1.__iter__()
# print(diedai)
# print(next(diedai))
# print(isinstance(diedai,Iterator))
# print(next(diedai))

#这是一个tuple类的实例化对象
# tuple1 = ('武强','李冲','陈明升','冯伟')
# help(tuple1)
# print(dir(tuple1))
# print(isinstance(tuple1,Iterable))
# diedai = tuple1.__iter__()
# print(isinstance(diedai,Iterator))
# print(next(diedai))
# print(next(diedai))

#这是一个字典类的实例化对象
# dict1 = {'a':1,'b':2,'c':3}
# help(dict1)
# print(dir(dict1))
# print(isinstance(dict1,Iterable))
# diedai = dict1.__iter__()
# print(isinstance(diedai,Iterator))
# print(next(diedai))
# print(next(diedai))

# 这是一个集合类的实例化对象
# set1 = {1,2,3,4,5,6,7,8,9,10,11,12}
# # help(set1)
# # print(isinstance(set1,Iterable))
# diedai = set1.__iter__()
# print(diedai)
# # print(isinstance(diedai,Iterator))
# print(next(diedai))
# print(next(diedai))


#打开的文件与上面类似
#什么是迭代器
    # 迭代器类里有两种方法['__iter__()','__next__']
    #迭代器可迭代
    #可以对迭代器再次使用__iter__方法，结果状态可以继承，可以认为就是一个迭代器
    #但是对列表使用多次__iter__时候，得到不同的迭代器，结果不可被继承

# #对迭代器使用__iter__会怎样,会继承
# diedai = diedai.__iter__()
# print(diedai)
# print(next(diedai))
#
# diedai = diedai.__iter__()
# print(diedai)
# print(next(diedai))
#
# #对列表多次使用__iter__(),会得到怎样的迭代器
# diedai1 = set1.__iter__()
# print(diedai1)
# print(next(diedai1))
#
# diedai1 = diedai1.__iter__()
# print(diedai1)
# print(next(diedai1))



# 生成器又是什么鬼
    # 生成器就是一种迭代器(i for i in range(10))
    # 从本质上讲，生成器是通过yield与(i for i in range(10))来封装起来的迭代器，
    # 换句话说就是把迭代器用人的语言风格封装起来，这样看起来就更加简洁了
    # 我们创造迭代器有这么几种方法：
    # 1:直接定义，里面包含['__iter__','__next__'],2:通过可迭代对象转化
    # 3:yield关键字；4:(i for i in range(10))
    # 为了研究方便，我们3,4方法实现的迭代器叫做生成器

# def fib():
#     a,b = 0,1
#     while True:
#         yield b
#         a,b = b,a+b
#
# x = fib()
# print(x)
# print(next(x))


#事实上，我们也可以通过['__iter__','__next__']来定义一个斐波那契数列
##########################################################
def hanshu():
    a = [(1,2,3),(4,5,6),(7,8,9),(10,11,12),(13,14,15)]
    for i in a:
        print(222)
        yield {
            'a':i[0],
            'b':i[1],
            'c':i[2]
        }

x = hanshu()
##########################################################
# dict1 = [{'a': 1, 'b': 2, 'c': 3},
#          {'a': 4, 'b': 5, 'c': 6},
#          {'a': 7, 'b': 8, 'c': 9},
#          {'a': 10, 'b': 11, 'c': 12},
#          {'a': 13, 'b': 14, 'c': 15}
#     ]
# x = dict1.__iter__()
# ##########################################################
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# for x0 in x:
#     print(x0)
#     print(111)



# print(next(x))
# print(next(x))
# x = [(1,2,3),(4,5,6),(7,8,9),(10,11,12),(13,14,15)]
# x = x.__iter__()
# print(next(x))
# y = x.__iter__()
# print(next(y))
# z = y.__iter__()
# for x0 in z:
#     print(x0)
#     print(111)


