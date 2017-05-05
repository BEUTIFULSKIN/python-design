#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_iterator.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/5 17:32
#
#     描述  : 迭代器模式 —— 提供一种方法依次访问聚合对象的内部元素，不直接暴露聚合对象的内部
#


class Other:
    def __init__(self, t_name, t_high, t_weight, t_age):
        self.name = t_name
        self.high = t_high
        self.weight = t_weight
        self.age = t_age

    def get_other_content(self):
        return [self.name, self.high, self.weight, self.age]


class A:
    def __init__(self, t_other):
        self.other_obj = t_other

    def to_count(self, num):
        other_attr = self.other_obj.get_other_content()
        for i, attr in zip(range(num), other_attr):
            yield attr


if __name__ == '__main__':
    other = Other('xixi', 168, 45, 16)
    a = A(other)
    two_attr_func = lambda: a.to_count(2)
    four_attr_func = lambda: a.to_count(4)

    for item in two_attr_func():
        print item

    print '#' * 40
    for item in four_attr_func():
        print item
