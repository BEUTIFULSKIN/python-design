#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_factory.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/3 14:02
#
#     描述  : 工厂模式
#


class Sender:
    def __init__(self):
        self.msg = None

    def set_msg(self, t_msg):
        self.msg = t_msg

    def send(self):
        return self.msg


class EmailSender(Sender):
    def set_msg(self, t_msg):
        self.msg = t_msg

    def send(self):
        return self.msg


class MessageSender(Sender):
    def set_msg(self, t_msg):
        self.msg = t_msg

    def send(self):
        return self.msg


# 提供一个统一调用的接口
class Provide(object):
    def p_send(self):
        return Sender()

    def p_recv(self):
        pass


class FactoryEmailSender(Provide):

    def p_send(self):
        return EmailSender()


class FactoryMessageSender(Provide):

    def p_send(self):
        return MessageSender()


if __name__ == '__main__':
    t_provide = FactoryEmailSender()
    email_sender = t_provide.p_send()
    email_sender.set_msg("hello yoke")
    msg = email_sender.send()
    print "msg: ", msg

    t_provide = FactoryMessageSender()
    mess_sender = t_provide.p_send()
    mess_sender.set_msg("how are you?")
    msg = mess_sender.send()
    print "msg: ", msg
