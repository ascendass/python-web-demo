#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


# 斐波那契数列
# 1，直接打印函数无返回，可复用性差，
def fab1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b, end=' ')
        a, b = b, a + b
        n += 1


# 2，最好不要用List来保存中间结果，以免内存问题，用iterable迭代更好
def fab2(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


# yield-generator，迭代函数返回值，代码从yield的下一句继续执行，函数的本地变量像是和中断之前一样
def fab3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


# 说明：yield from iterable本质上等于for item in iterable: yield item的缩写版


def f_wrapper(f):
    print('\n使用yield from代替for循环')
    yield from f


def f_wrapper_multi(x):
    print('yield from包含多个子程序')
    yield from range(x, 0, -1)  #逆序
    yield from range(x)


# 例5 利用yield from语句向生成器（协程）传送数据
# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，换回生产者继续生产，效率极高：
def consumer_work(len):
    # 读取send传进的数据，并模拟进行处理数据
    print("writer:")
    w = ''
    while True:
        w = yield w  # w接收send传进的数据,同时也是返回的数据
        print('[CONSUMER] Consuming %s...>> ', w)
        w *= len  # 将返回的数据乘以100
        time.sleep(0.1)


def consumer(coro):
    yield from coro  # 将数据传递到协程(生成器)对象中


def produce(c):
    c.send(None)  # "prime" the coroutine
    for i in range(5):
        print('[Producer] Producing %s----', i)
        w = c.send(i)  # 发送完成后进入协程中执行
        print('[Producer] Receive %s----', w)
    c.close()


if __name__ == '__main__':
    f = fab3(5)
    for n in f:
        print(n, end=' ')
    print('\n---------------------')
    wrap = f_wrapper(fab3(5))
    for i in wrap:
        print(i, end=' ')
    print('\n---------------------')
    print(list(f_wrapper_multi(5)))
    print('\n---------------------')
    c1 = consumer_work(100)
    produce(c1)
