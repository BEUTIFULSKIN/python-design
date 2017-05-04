#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-03 17:15:08
# @Author  : Yi Wang (gzytemail@126.com)
# @Link    : https://github.com/wang2222qq
# @des     : 装饰器模式
"""
案例:
在咖啡店中
1.咖啡有很多种类.
2.咖啡搭配的调味品也有很多种
3.要获取客户的消费
"""

# Abstract class
class Coffee:
    def cost(self):
        pass


class Cappuccino(Coffee):
    """
    卡布奇诺
    """
    def cost(self):
        return 2.5


class Latte(Coffee):
    """
    拿铁
    """
    def cost(self):
        return 2.2


class Dressing():
    """调味料"""
    def __init__(self, office):
        self._office = office

    def cost(self):
        return self._office.cost()


class Milkshake(Dressing):
    """奶昔"""
    def cost(self):
        return self._office.cost() + 0.2


class Suger(Dressing):
    """白糖"""
    def cost(self):
        return self._office.cost() + 0.1


def client():
    coffee = Cappuccino()
    coffee = Milkshake(coffee)
    coffee = Milkshake(coffee)
    coffee = Suger(coffee)
    print("total money:%s" % coffee.cost())


if __name__ == '__main__':
    client()




        
        





