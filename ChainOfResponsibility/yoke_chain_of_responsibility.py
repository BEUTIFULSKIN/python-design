#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_chain_of_responsibility.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/3 16:50
#
#     描述  : 责任链模式 —— 为一个请求提供多种响应处理, 类似于轮询处理
#     例子  : 创建服务单
#                       售后服务单（经销商）
#                       客服服务单（客服）
#                       快递服务单（仓库）


# 人员权限判断，要拥有[ after_sale， service， express]这些权限才可以进行处理
def judge_user(func):
    def wrapper(*args, **kwargs):
        limit_list = ['after_sale', 'service', 'express']
        user = args[1]
        if user in limit_list:
            return func(*args, **kwargs)
        print "have no type %s of create invoice " % user
    return wrapper


class Handle:
    def __init__(self):
        self._successor = None

    def successor(self, t_successor):
        self._successor = t_successor


class HandleAfterSaleInvoice(Handle):
    @judge_user
    def handle(self, user):
        if user == 'after_sale':
            print "enter create after sale invoice port"
        else:
            self._successor.handle(user)


class HandlerServiceInvoice(Handle):
    @judge_user
    def handle(self, user):
        if user == 'service':
            print "enter create service invoice port"
        else:
            self._successor.handle(user)


class HandlerExpressInvoice(Handle):
    @judge_user
    def handle(self, user):
        if user == 'express':
            print "enter create express invoice port"
        else:
            self._successor.handle(user)


if __name__ == '__main__':
    a_s_h = HandleAfterSaleInvoice()
    s_h = HandlerServiceInvoice()
    e_h = HandlerExpressInvoice()

    a_s_h.successor(s_h)
    s_h.successor(e_h)

    user_type_list = ['service', 'hello', 'express', 'world', 'after_sale']
    for item in user_type_list:
        a_s_h.handle(item)






