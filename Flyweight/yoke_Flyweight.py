#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_Flyweight.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/2 18:12
#
#     描述  : 享元模式——Flyweight
#     意图  : 减少对象的循环引用导致的内存过大
#
import weakref


class AllotObj(object):
    _allot_dict_ = weakref.WeakValueDictionary()

    def __new__(cls, value, msg):
        obj = AllotObj._allot_dict_.get(str(value+msg), None)
        if not obj:
            obj = object.__new__(cls)
            obj.value, obj.msg = value, msg
            cls._allot_dict_[str(value+msg)] = obj
        return obj

    def __repr__(self):
        return "<AllotObj %s %s>" % (self.value, self.msg)


if __name__ == '__main__':
    a_1 = AllotObj('10', 'hello')
    a_2 = AllotObj('10', 'hello')
    print a_1 is a_2
    print (a_1 == a_2)
    print id(a_1), id(a_2)

