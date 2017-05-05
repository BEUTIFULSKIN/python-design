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
import random


class Other:
    def __init__(self):
        self._name = None
        self._high = None
        self._weight = None
        self._age = None
        self.choose_one()

    def choose_one(self):
        self._name = random.choice(['xixi', 'wangwang', 'hehe'])
        self._high = random.randint(155, 170)
        self._weight = random.randint(45, 60)
        self._age = random.randint(15, 20)

    def _get_other_content(self):
        return [self._name, self._high, self._weight, self._age]

    def to_count(self, num):
        other_attr = self._get_other_content()
        for i, attr in zip(range(num), other_attr):
            yield attr


if __name__ == '__main__':
    other = Other()
    two_attr_func = lambda: other.to_count(2)
    four_attr_func = lambda: other.to_count(4)

    for item in two_attr_func():
        print item

    print '#' * 40
    for item in four_attr_func():
        print item
