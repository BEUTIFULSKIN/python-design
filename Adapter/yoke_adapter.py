#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_adapter.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/5 10:58
#
#     描述  : 适配器模式 —— 对两个类的接口进行兼容，是一个事后诸葛
#


class Plug:
    def __init__(self):
        self.pulg_type = None

    def get_plug_type(self):
        return self.pulg_type


class GermanyPlug(Plug):
    def __init__(self):
        Plug.__init__(self)
        self.pulg_type = "Germany"

    def use_two_circular_plug(self):
        """ 两头圆形插头 """
        pass


class ChinesePlug(Plug):
    def __init__(self):
        Plug.__init__(self)
        self.pro_area = "Chinese"

    def use_three_flat_shape_plug(self):
        """ 三头扁形插头 """
        pass


class ChangePlugAdapter:
    def __init__(self):
        self.to_change_type = None

    def chinese_change_germany(self, chinese_plug):
        if chinese_plug == 'Chinese':
            g_p = GermanyPlug()
            g_p.use_two_circular_plug()
            print "chinese plug change to germany"
        else:
            print "can not use obj of chinese type"


class Client:
    def __init__(self):
        self.name = None  # 姓名
        self.nationality = None  # 国籍
        self.gender = None  # 性别
        self.age = None  # 年纪

    def inital_identity(self, t_name, t_nation, t_sex, t_age):
        self.name = t_name
        self.nationality = t_nation
        self.gender = t_sex
        self.age = t_age


class GermanyHotel:
    def __init__(self, t_client):
        self.client = t_client

    def use_plug_by_nation(self):
        p = ChangePlugAdapter()
        p.chinese_change_germany(self.client.nationality)


if __name__ == '__main__':
    c = Client()
    c.inital_identity("xiaoming", "Chinese", "boy", 18)
    hotel_client = GermanyHotel(c)
    hotel_client.use_plug_by_nation()