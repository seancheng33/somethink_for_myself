'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/18
@Program      : 练习yeild的实例，一个简单的生产者与消费者程序
'''
import random


def producer():
    while True:
        data = random.randint(0, 9)
        print('生产了：', data)
        yield data


def consumer():
    while True:
        data = yield
        print('消费了：', data)


def clerk(jobs, producer, consumer):
    print('执行 {} 次生产与消费'.format(jobs))
    p = producer()
    c = consumer()
    next(c)
    for i in range(jobs):
        data = next(p)
        c.send(data)


clerk(30, producer, consumer)
