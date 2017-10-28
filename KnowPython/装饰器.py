#装饰器
# 装饰器的就是一个函数，神码样的函数呢？
# 装饰器让其他函数不需要任何代码变动的情况下，增加一些功能，装饰器的
# 返回值也是一个函数
# 应用：插入日志/性能测试/缓存/...
# 装饰器也有封装解藕的思想，不允许修改原来的函数的情况下对函数功能进行扩充
# 下面先举个例子：

# 为了加强立理解，下面遮盖共识你需要达成
# 数字，字符串等是一个对象，函数也是一个对象，数字可以命名给一个变量，
# 函数也可以赋值给一个变量，这个变量就是一个函数

# 招生了，阴差阳错，机缘巧合，很多跟我一样的学员来兄弟连了，目前还没上课。
def xueyuan1():
    print('老子要学python，要不然找不到媳妇')

def xueyuan2():
    print("老子也要学python，要不然找不到媳妇")

def xueyuan3():
    print("老子也要")

# ...一帮想要的兄弟来到了兄弟连...
# 开学第一天李超为了摸大家的底，让每个兄弟写一个装饰器，由于大家基础参差不齐，而且0基础
# 所以基本是空白的，每个人都是一个功能不同，基础不一样的函数，如下

def xueyuan1():
    print('老子要学python，要不然找不到媳妇')

def xueyuan2():
    print("老子也要学python，要不然找不到媳妇")

def xueyuan3():
    print("老子也要")

# 开始考试
xueyuan1()
xueyuan2()
xueyuan3()

# 考完了，草他妈，啥都不会，这媳妇很是个迷茫啊，怎么办？王晟有话说：
# 兄弟连给大家提供一个场所，大家交2万开始自学吧，自己来装饰自己吧

def xueyuan1():
    print('老子要学python，要不然找不到媳妇')
    print('开始在四楼自学了,老子在研究装饰器')

def xueyuan2():
    print("老子也要学python，要不然找不到媳妇")
    print('开始在四楼自学了,老子在研究装饰器')

def xueyuan3():
    print("老子也要")
    print('开始在四楼自学了,老子在研究装饰器')

# 十天后...
# 这哥们被老板炒了

# 这个时候陈玉龙有话说
# 那个王晟真是哥傻子，为啥有啥要让他们自学呢
# 玉龙兄说，我给学生上课吧，一定要让大家培养一种思想
# 对，思想，然后大家自己慢慢琢磨吧，不要老是想着坐到那里让老师给你罐知识
# 我草拟大爷

def ziliao_and_fangfa():
    print('十天4行代码，我教给大家的都是方法')

def xueyuan1():
    print('老子要学python，要不然找不到媳妇')
    ziliao_and_fangfa()

def xueyuan2():
    print("老子也要学python，要不然找不到媳妇")
    ziliao_and_fangfa()

def xueyuan3():
    print("老子也要")
    ziliao_and_fangfa()

# 十天过去了...被李超炒了
# 唉...李超有话说：
# 学生就是一个一个毛胚，原材料，老师可以蹂躏，大家都是0基础，连知识都没有
# 他妈哪里来的能力去独自创新，独立思考？
# 针对这个0基础的学生，我就是认为，他们就是面板上的一坨面，想把他们揉成什么样子
# 就靠你们这些拿工资的
def xdljgc(func):
    def xue_jineng():
        print('django框架贼简单')
        print('装饰器小儿科')
        print('游刃有余，我最近在研究人工智能')

        return xueyuan1()

    return xue_jineng


@xdljgc
def xueyuan1():
    print('老子要学python，要不然找不到媳妇')
@xdljgc
def xueyuan2():
    print("老子也要学python，要不然找不到媳妇")
@xdljgc
def xueyuan3():
    print("老子也要")


# 看得出来李超的基本思想就是
# 1：封装------规定已经实现的功能代码不允许被修改
# 2：开放------高可扩展，允许通过别的方法给原函数添加功能

# 在兄弟连培训完，工作都找不到，python01期的都需要被就业老师装饰
# 总的来说，兄弟连有专门的装饰部门


# 装饰器进化史：论一个装饰器的自我修炼
# 1：爆炸前夕：嵌套函数
# python中函数是支持嵌套的，也就是可以在函数内部定义一个函数，如下：
#定义一个外层函数
def foo():
    #定义一个内部函数
    def bar():
        print('hello world')
#当然，函数的本质就是个变量，只是指向变量地址的是一个函数
def foo():
    def bar():
        print('hello world')
    #将函数bar返回
    return bar
func = foo()
func()

#2：爆炸前夕：酝酿中的闭包
def foo():
    name = 'Amar'
    #定义一个内部函数
    def bar():
        #虽然bar函数中没有定义name变量，但是它可以访问外部函数的局部变量
        print(name)
    return bar
func = foo()
func()

# 3:闭包形态2