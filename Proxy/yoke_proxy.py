#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_proxy.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/3 16:51
#
#     描述  : 代理模式 —— 对访问的对象提供了一种代理以控制对象的访问
#


class Proxy(object):
    def __init__(self):
        self.content = None

    def __str__(self):
        return "tip to you: %s", self.content


class ChildProxy(Proxy):
    def __init__(self):
        Proxy.__init__(self)
        self.content = "resource show for child or adult"


class AdultProxy(Proxy):
    def __init__(self):
        Proxy.__init__(self)
        self.content = "resource only show for adult"


class RouteProxy:
    def __init__(self):
        self.to_proxy = None

    def choose_route(self, u_type):
        if u_type == 'child':
            self.to_proxy = ChildProxy()
        elif u_type == 'adult':
            self.to_proxy = AdultProxy()
        return self.to_proxy

if __name__ == '__main__':
    route = RouteProxy()
    child_proxy = route.choose_route('child')
    print child_proxy.__str__()

    adult_proxy = route.choose_route('adult')
    print adult_proxy.__str__()
