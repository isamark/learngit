# 论进程


# 多任务
# 单个cpu能完成多个任务的核心原因就是操作系统在极其短的时间进行任务切换，别人感觉是每个程序在同时执行
# 上面这种算法叫时间片轮转
# 当然还有一个优先级调度，也就是操作系统会优先让有的程序先运行

# 还有一个词语，并发与并行
# 并发指的是当前任务数大于核数，不大于就是并行


# 先从fork开始
import os
import time
import random


# res = os.fork()
# print('哈哈')
# 打印结果为：两个哈哈，至于是谁的哈哈，那就不一定了

# 再来写一个程序：
# res = os.fork()
# if res == 0:
#     while True:
#         print('-----子进程在运行-----')
#         time.sleep(1)
#
# else:
#     while True:
#         print('-----主进程在运行-----')
#         time.sleep(1)
#
# 总结：
# res = os.fork()这句代码会生一个孩子出来，我们叫他为子进程，他跟妈妈从这里一起执行下面的代码
# 但是子进程的返回值为０，所以只会运行if里面的代码，主进程res的值大于零


# 继续写程序
# res = os.fork()
# if res == 0:
#     print('-----子进程在运行-----')
#     time.sleep(1)
#     print('-----子进程over-----')
#
# else:
#     print('-----主进程在运行-----')
#
# print('-----over-----')

# amar@cool:~$ vim test.py
# amar@cool:~$ python test.py
# -----主进程在运行-----
# -----over-----
# -----子进程在运行-----
# amar@cool:~$ -----子进程over-----
# -----over-----

# 总结：
# 主进程不会等待子进程，有可能会提前结束

# 可以认为百度为每个同一时刻访问服务器的用户分配了一个进程


# 继续了　关于子进程能否与主进程通信
# g_num = 100
# res = os.fork()
# if res == 0:
#     print('-----1-----')
#     g_num += 1
#     print('-----1-----%d'%g_num)
#
# else:
#     time.sleep(3)
#     print('-----2-----%d'%g_num)

# 总结：主进程与子进程里面的变量互不干扰，子进程改变了g_num变为101,但是主进程仍然是原来的大小


# 多个fork
# 主进程执行下面这句话会产生一个子进程
# res = os.fork()
# if res == 0:
#     print('-----1-----')
#
# else:
#     print('-----2-----')
#
# # 主进程与子进程同时运行下面的代码
# res = os.fork()
# if res == 0:
#     # 二儿子执行
#     # 孙子执行(一儿子的儿子)
#     print('-----11-----')
#
# else:
#     # 父亲自己执行
#     # 一儿子执行
#     time.sleep(2)
#     print('-----22-----')

# 分析
# 第二个fork相当于主进程与子进程同时又开了一个子进程

# 如果改为下面代码呢

# res = os.fork()
# if res == 0:
#     print('-----1-----')
#
# else:
#     print('-----2-----')
#     res = os.fork()
#     if res == 0:
#         print('-----11-----')
#
#     else:
#         print('-----22-----')

# 下面这个是只在父进程里面开一个二儿子进程



# 如果你打算写多进程的服务程序，Unix/Linux无疑是正确的选择，但是由于windows不能用fork，
# 难道Windows无法用python编写多进程程序吗，但事实是python就是跨平台的，自然提供了跨平台
# 的多进程支持，multiprocess模块就是跨平台的多进程模块

# 下面咱们研究这一模块
from multiprocessing import Process


# def test():
#     while True:
#         print('-----1-----')
#         time.sleep(2)
#
# p = Process(target=test)
# p.start()   #子进程回去运行taeget里面的函数，主进程继续向下运行，这句是一个分叉
#
# while True:
#     print('-----main-----')
#     time.sleep(2)

# 总结：这是一个基本的过程

# def test():
#     for i in range(5):
#         print('-----1-----')
#         time.sleep(2)
#
# p = Process(target=test)
# p.start()

# 总结：
# Process与fork的区别
# fork主进程不会等到子进程运行完才结束，Process主进程会等子进程结束才会结束，但是这并不代表主进程等待子进程


# 继续
# 如何在子进程执行时间不确定的时候，让子进程执行完，主进程再执行
# 睡觉是不能满足的，因为主进程怎么会知道要睡多久
# 所以引入了join,专业词语叫堵塞

# def test():
#     for i in range(random.randint(1,5)):
#         print('-----1-----')
#         time.sleep(2)
#
# p = Process(target=test)
# p.start()
# p.join(1)
# print('-----主进程-----')

# 总结：
# join可以让子进程运行完后主进程再运行


# 如果强制让一个子进程结束呢：
# terminate(),不管任务是否完成，立即终止
# def test():
#     for i in range(random.randint(1,5)):
#         print('-----1-----')
#         time.sleep(2)
#
# p = Process(target=test)
# p.start()
# p.terminate()
# print('-----主进程-----')

# 总结：不管任务是否完成，立即终止


# 上面方式创建子进程都是实例化的时候把想要在子进程中运行的代码当参数传入类中
# 事实上
# 用Process创建子进程还有一种方式就是通过类直接创建，创建完后直接实例化
# 然后再start()

# class MyNewProcess(Process):
#     def run(self):
#         while True:
#             print('-----1-----')
#             time.sleep(2)
#
# p = MyNewProcess()
# p.start()
#
# while True:
#     print('-----main-----')
#     time.sleep(2)

# 总结：
# p.start()  这里的start方法在父类Process里面，运行这个函数就会调用run方法


# 下面学习著名的进程池
# 上面刚才学到的都是创建子进程的方式无论是multiprocess中的Process还是fork,都是适用于
# 创建数量不多的进程，但是如果是很多，上千个进程呢，手动去创建进程的工作量太大，此时就可以用到
# multiprocess中的Pool方法

# 初始化Pool时，可以指定一个最大的进程数

from multiprocessing import Pool

def worker(num):
    for i in range(2):
        print('-----%d-----'%num)
        time.sleep(2)

# ２表示进程池最多只能有２个进程同时进行
pool = Pool(4)

for i in range(12):
    print('-----%d-----'%i)

    pool.apply_async(worker,(i,))
    # 注意：
    # 如果添加的任务数量超过了进程池中进程的数量，那么不会导致添加不进去
    # 添加到进程中的任务，如果还没有被执行的话，那么此时，他们会等待进程池中的进成完成一个任务后，
    # 会自动用刚才那个进程，完成当前的新任务

    #　添加十个进程仍在进程池里面，虽然每次只能执行２个进程，就相当与只有两个人干活，但是现在有一堆进程，每次他们只能干两件

print('-----start-----')
pool.close() #关闭进程池，相当于不能再次添加新任务了，准备运行拉，其实进程从这里开始运行，
pool.join() #等待pool子进程运行完后再运行主进程
print('-----end-----')



# 多种方式的对比
# 方式一
# res = os.fork()
# if res == 0:
#     print('-----1-----')
# else:
#     print('-----3-----')
#
# # 方式２
# p = Process(target=function)
# p.start()
#
# #　方式３
# pool = Pool(3)
# pool.apply_async(function,kwds=n)






