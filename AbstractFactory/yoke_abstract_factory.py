#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_abstract_factory.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/3 15:12
#
#     描述  : 抽象工厂
#


# 抽象的产品类
class Product:
    def __init__(self):
        self.size = None
        self.price = None
        self.band = None

    def set_info(self, t_size=None, t_price=None, t_band=None):
        self.size = t_size
        self.price = t_price
        self.band = t_band

    def show_size(self):
        return self.size

    def show_price(self):
        return self.price

    def get_band(self):
        return self.band

    def show_all_info(self):
        print "pro size: ", self.size
        print "pro price: ", self.price
        print "pro band: ", self.band


# 由产品基类派生出来的鼠标和键盘
class Mouse(Product):
    def __init__(self):
        Product.__init__(self)

    def set_microsoft_product(self):
        self.set_info(t_size=10,
                      t_price=150,
                      t_band="Microsoft")

    def set_panasonic_product(self):
        self.set_info(t_size=10,
                      t_price=100,
                      t_band="Panasonic")


class Keyboard(Product):
    def __init__(self):
        Product.__init__(self)

    def set_logitech_product(self):
        self.set_info(t_size=100,
                      t_price=50,
                      t_band="Logitech")

    def set_dell_product(self):
        self.set_info(t_size=100,
                      t_price=30,
                      t_band="Dell")


# 抽象工厂类
class AbstractFactory:
    def __init__(self):
        self.product = None

    def get_m_product(self):
        return self.product

    def get_k_product(self):
        return self.product

    def get_product(self):
        return self.product


# A。B类型工厂继承于抽象工厂类
class AFactory(AbstractFactory):
    def __init__(self):
        AbstractFactory.__init__(self)
        self.product = None

    def get_m_product(self):
        self.product = Mouse()
        self.product.set_microsoft_product()
        return self.get_product()

    def get_k_product(self):
        self.product = Keyboard()
        self.product.set_logitech_product()
        return self.get_product()


class BFactory(AbstractFactory):
    def __init__(self):
        AbstractFactory.__init__(self)
        self.product = None

    def get_m_product(self):
        self.product = Mouse()
        self.product.set_panasonic_product()
        return self.get_product()

    def get_k_product(self):
        self.product = Keyboard()
        self.product.set_dell_product()
        return self.get_product()


if __name__ == '__main__':
    a_fac = AFactory()
    print "--------A factory prodce Mouse----------"
    a_m_pro = a_fac.get_m_product()
    a_m_pro.show_all_info()
    print "--------A factory prodce KAeybroad------"
    a_k_pro = a_fac.get_k_product()
    a_k_pro.show_all_info()
    print "--------B factory prodce Mouse----------"
    b_fac = BFactory()
    b_m_pro = b_fac.get_m_product()
    b_m_pro.show_all_info()
    print "--------B factory prodce Keybroad-------"
    b_k_pro = b_fac.get_k_product()
    b_k_pro.show_all_info()
