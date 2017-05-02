#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_decorate.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/2 18:07
#
#     描述  : 装饰器 Decorator 模式
#     意图  : 动态地给一个对象添加一些额外的职责。就增加功能来说，Decorator 模式相比生成子类更为灵活。


class Foo(object):

    def f1(self):
        return 'original f1'

    def f2(self):
        return 'original f2'

    def hello(self):
        print "hello world"
        return "ni hao"


class Decorator(object):
    def __init__(self, obj):
        self.decorator_obj = obj

    def f1(self):
        return self.decorator_obj.f1()

    def __getattr__(self, name):
        return getattr(self.decorator_obj, name)


if __name__ == '__main__':
    f = Foo()
    decorator = Decorator(f)
    print decorator.f1()
    print decorator.f2()
    func = decorator.__getattr__('hello')
    print func()
