#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_builder.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/2 18:12
#
#     描述  : Building Model
#     意图  : 将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
#


class Product(object):
    def __init__(self, t_name, t_type):
        self.name = t_name
        self.type = t_type

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type


class Aproduct(Product):
    def __init__(self, t_name, t_type):
        Product.__init__(self, t_name, t_type)
        self.size = 0

    def set_size(self, t_size):
        self.size = t_size

    def set_price(self, t_price):
        self.price = t_price


class AproductOne(Aproduct):
    def __init__(self, t_name, t_type):
        Aproduct.__init__(self, t_name, t_type)

    def show_product(self):
        print self.get_name()
        print self.get_type()
        print self.size
        print "this is A-one product"


class AproductTwo(Aproduct):
    def __init__(self, t_name, t_type):
        Aproduct.__init__(self, t_name, t_type)

    def show_product(self):
        print self.get_name()
        print self.get_type()
        print self.size
        print "this is A-two product"


class Bproduct(Product):
    def __init__(self, t_name, t_type):
        Product.__init__(self, t_name, t_type)
        self.price = 0.0

    def set_price(self, t_price):
        self.price = t_price

    def set_size(self, t_size):
        self.size = t_size


class BproductOne(Bproduct):
    def __init__(self, t_name, t_type):
        Bproduct.__init__(self, t_name, t_type)

    def show_product(self):
        print self.get_name()
        print self.get_type()
        print self.price
        print "this is B-one product"


class BproductTwo(Bproduct):
    def __init__(self, t_name, t_type):
        Bproduct.__init__(self, t_name, t_type)

    def show_product(self):
        print self.get_name()
        print self.get_type()
        print self.price
        print "this is B-two product"


class Director(object):
    def __init__(self):
        self.builder = None

    def constract_building(self):
        self.builder.set_price(10)
        self.builder.set_size(100)

    def get_building(self):
        return self.builder.show_product()


if __name__ == '__main__':
    abstract_obj = Director()
    # A-one product
    abstract_obj.builder = AproductOne('AS1', 'P001')
    abstract_obj.constract_building()
    abstract_obj.get_building()
    # B-one product
    abstract_obj.builder = BproductOne('BS1', 'P002')
    abstract_obj.constract_building()
    abstract_obj.get_building()
    # A-two product
    abstract_obj.builder = AproductTwo('AS2', 'P003')
    abstract_obj.constract_building()
    abstract_obj.get_building()
    # B-two product
    abstract_obj.builder = BproductTwo('BS2', 'P004')
    abstract_obj.constract_building()
    abstract_obj.get_building()