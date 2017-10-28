#先写一个for循环
# for x in [1,2,3,4,5,6,7,8,9]:
#     print(x)

# for循环的底层
i = [1,2,3,4,5,6,7,8,9].__iter__()
while True:
    try:
        x = i.__next__()
        print(x)
    except StopIteration:
        break

# 得到：
    #列表是一个对象，一个可迭代的对象，先通过__iter__方法转化为一个迭代器
    #然后再通过while与__next__()循环取出