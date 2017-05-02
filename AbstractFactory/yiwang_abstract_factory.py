#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-02 17:35:49
# @Author  : Yi Wang (gzytemail@126.com)
# @Link    : https://github.com/wang2222qq
# @des     : 抽象工厂模式
"""
APA --> A_1
|   --> A_2

APB --> B_1
|   --> B_2

AF  --> FactoryA
|   --> FactoryB

FactoryA --> A_1  B_1
FactoryB --> A_2  B_2
"""


# Abstruct Product A
class APA(object):
    def __init__(self):
        pass

    def create(self):
        pass


# Abstruct Product B
class APB(object):
    def __init__(self):
        pass

    def create(self):
        pass


# Product A_1
class PA1(APA):
    def __init__(self):
        print("create PA1 instance")

    def create(self):
        print("making a Product A1")

# Product A_1
class PA2(APA):
    def __init__(self):
        print("create PA2 instance")

    def create(self):
        print("making a Product A2")

    
# Product B_1
class PB1(APB):
    def __init__(self):
        print("create PB1 instance")

    def create(self):
        print("making a Product B1")


# Product B_2
class PB2(APB):
    def __init__(self):
        print("create PB2 instance")

    def create(self):
        print("making a Product B2")


# Abstruct Factory Class
class AF(object):
    def __init__(self):
        pass

    def make_product_a(self):
        pass

    def make_product_b(self):
        pass


# Factory A
class FactoryA(AF):
    def __init__(self):
        pass

    def make_product_a(self):
        return PA1()

    def make_product_b(self):
        return PB1()


# Factory B
class FactoryB(AF):
    def __init__(self):
        pass

    def make_product_a(self):
        return PA2()

    def make_product_b(self):
        return PB2()


def product_process():
    for cls in [FactoryA, FactoryB]:
        f = cls()
        # get Product A instance
        a = f.make_product_a()
        a.create()
        # get Product B instance
        b = f.make_product_b()
        b.create()


if __name__ == "__main__":
    product_process()
