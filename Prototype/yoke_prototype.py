#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_prototype.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/3 16:53
#
#     描述  : 原型模式，拷贝对象，拷贝有深浅
#
import copy


class Prototype:
    def __init__(self):
        self._pro_dict = {}

    def set_proto_obj(self, name, obj):
        if not self._pro_dict.get(name, None):
            self._pro_dict[name] = obj

    def get_proto_obj(self, name):
        if self._pro_dict.has_key(name):
            return self._pro_dict.get(name, None)
        return None

    def copy_obj(self, t_name, **kwargs):
        obj = self.get_proto_obj(t_name)
        if obj:
            new_obj = copy.deepcopy(obj)
            new_obj.__dict__.update(kwargs)
            return new_obj


class UseTestPrototype:
    def __init__(self, t_name):
        self.name = t_name

    def show_name(self):
        print self.name

    def __repr__(self):
        print "<UseTestPrototype %s>", self.name


if __name__ == '__main__':
    t_proto = UseTestPrototype("May")
    t_proto.show_name()
    create_proto = Prototype()
    create_proto.set_proto_obj('Test', t_proto)
    new_obj = create_proto.copy_obj('Test', name="June")
    new_obj.show_name()
