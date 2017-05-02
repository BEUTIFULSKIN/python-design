#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-02 17:43:52
# @Author  : Yi Wang (gzytemail@126.com)
# @Link    : https://github.com/wang2222qq
# @des     : 工厂模式


class ProductA:
    """ 
    产品A
    """
    def __init__(self):
        pass

    def product(self):
        print("生产一个产品A")


class ProductB:
    """ 
    产品B
    """
    def __init__(self):
        pass

    def product(self):
        print("生产一个产品B")


class Factory(object):
    """ 
    工厂
    """
    def __init__(self):
        pass

    @staticmethod
    def make_product(material):
        if material == "A":
            return ProductA()
        elif material == "B":
            return ProductB()
        else:
            raise ValueError("the material can't made product")


if __name__ == "__main__":
    factory = Factory()
    # make product A
    factory.make_product("A").product()
    # make product B
    factory.make_product("B").product()
