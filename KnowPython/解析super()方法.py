# 关于super()方法
#
# class Father():
#     def driver(self):
#         print(self,2)
#         print('去送煤')
#
#
# class Son(Father):
#     def papa(self):
#         print(self,1)
#         print('papapa')
#         super().driver()
#
# son = Son()
# son.papa()
# print(isinstance(son,Father))
# print(isinstance(son,Son))
#
# class Animal(object):
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(self)
#         print('Hello, I am %s.' % self.name)
# class Dog(Animal):
#     def greet(self):
#         super().greet()
#         print('WangWang...')
#     def b(self):
#         super().greet()
#         print('WangWang...')
#
#
# dog = Dog('dog')
# dog.greet()
#
# a = Animal('33')
# a.greet()
# dog.b()

# 我想解释虾上面的全过程

# python解释器发动机已启动，一行一行走，一路上可执行的啥都没有
# 直到这哥们碰到dog = Ｄog('dog')
# 开始实例化，先运行Dog里面的__new__()方法得到一个Ｄog的实例化对象
# 然后再运行Ｄog里面的__init__(),把__new__()方法得到的实例化对象当参数传入
# 刚开始我还以为实例化时候就跑去父类Animal找__init__方法了，事实上已经继承过来了，哈哈哈
# 然后就顺利的初始化了，然后神码也不会打印出现

# 然后接下来运行dog.greet()，然后调用Ｄog里面的greet方法，进去之后，解释器发现了super().greet()
# 这哥们，这一步就相当于一个装饰器里面被装饰的函数，函数就是父类的greet方法(但是这不是装饰器)，如下：
# def greet(self):
#     print(self)
#     print('Hello, I am %s.' % self.name)
# 外面还有一层greet函数,与装饰器函数有些神似，毫无疑问两层greet函数的self均为dog对象，
# 运行完父类greet函数后，马上执行＂print('WangWang...')＂，
# 完毕！！！

# 以上算是对super()函数的初步了解
# 或许看完了，您还是对super有很多疑问，这玩意咋就这么神奇呢？，您可能会脱口说出一句概括super的话
# ：子类已经覆盖父类某某方法的时候，实现父类中该方法的调用，没错这就是你认为的super

# 而这是事实吗？
# 一会揭晓吧，先来看看一个例子

class Internet:
    def __init__(self):
        print('互联网改变世界')
        print('我正站在此风口上')

class FaceBook(Internet):
    def __init__(self):
        print('脸书目前有２０亿用户')
        super().__init__()
        print('连接全球')

class Google(Internet):
    def __init__(self):
        print('谷歌是一家改变世界的公司')
        super().__init__()
        print('是否能成为互联网霸主')

class AI(FaceBook,Google):
    def __init__(self):
        print('AI时代来了')
        super().__init__()
        print('我正在学习python,未来前途大大的')


print(AI.mro())
ai = AI()
# print(AI)
# print(ai.__class__)

# 兄弟看到了吧，super()并不是特指父类，好像有一个规则，什么规则呢？那就是＂MRO 列表＂
# 这玩意是什么鬼？
# 事实上，你所定义的任何一个类，python会计算出一个＂方法解析顺序列表＂就是＂MRO 列表＂
# print(AI.mro())
# 打印结果为：[<class '__main__.AI'>, <class '__main__.FaceBook'>, <class '__main__.Google'>, <class '__main__.Internet'>, <class 'object'>]
# 继承规则通过＂C3线性化算法＂计算得到，比较复杂，暂时不做研究
# 补充：＂MRO 列表＂其实就是合并所有父类的列表，只是有一套排序规则.



# super()的本质

# def super(cls,inst):
#     mro = inst.__class__.mro()
#     return mro[mro.index(cls) + 1]

# 这样super()得到的结果应该是一个类
# 可是
# super().__init__()为什么缺偏偏不传参数呢

# 询问老齐后，他说super()是对象，
# 我目前认为:
# super()返回值是一个类,__init__()也传参数了，只是这种会默认传一个对象对象














