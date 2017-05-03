#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_singleton.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/3 15:24
#
#     描述  : 单例模式
#
import random


class OnlyOwner(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # 原来的写法
            # org = super(OnlyOwner, cls)
            # cls._instance = org.__new__(cls, args, kwargs)
            # 调整后的写法
            cls._instance = object.__new__(cls, args, kwargs)
        return cls._instance

    def __init__(self):
        self.id = None

    def get_id(self):
        return self.id

    def __repr__(self):
        print "<OnlyOwner %s>" % self.id


class SingletonTest(OnlyOwner):
    def __init__(self):
        OnlyOwner.__init__(self)
        self.id = random.randint(1, 100)

    def show_id(self):
        return self.id

    def __repr__(self):
        print "<Test %s>" % self.id

if __name__ == '__main__':
    obj_1 = SingletonTest()
    print obj_1.get_id()

    obj_2 = SingletonTest()
    print obj_2.get_id()
    print obj_1 is obj_2
    print id(obj_1), id(obj_2)
