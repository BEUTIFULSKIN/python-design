#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_bridge.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/5 14:00
#
#     描述  : 桥连接模式，由桥衍生出多种情形下的具体实现的类
#             Bridge 模式把两个角色之间的继承关系改为了耦合的关系，
#             从而使这两者可以从容自若的各自独立的变化，这也是Bridge模式的本意。
#     例子  : 制造组装苹果手表，一个表可以组合多种表带


# Abstract Bridge
class AppleWatchBridge:
    def __init__(self):
        self.core = None
        self.version = None
        self.watchband = None

    def combine_watch(self, t_core, t_band):
        self.core = t_core
        self.watchband = t_band
        self.version = self.core.get_series_no() + self.watchband.get_series_no()

    def show_version(self):
        print self.version


# 手表核心组件
class WatchCoreTypeOne:
    def __init__(self, m_code, m_price, m_s_n):
        self.material_code = m_code
        self.price = m_price
        self.series_no = m_s_n

    def get_series_no(self):
        return self.series_no


class WatchCoreTypeTwo:
    def __init__(self, m_code, m_price, m_s_n):
        self.material_code = m_code
        self.price = m_price
        self.series_no = m_s_n

    def get_series_no(self):
        return self.series_no


# 手表表带
class WatchBandTypeOne:
    def __init__(self, m_code, m_price, m_s_n):
        self.material_code = m_code
        self.price = m_price
        self.series_no = m_s_n

    def get_series_no(self):
        return self.series_no


class WatchBandTypeTwo:
    def __init__(self, m_code, m_price, m_s_n):
        self.material_code = m_code
        self.price = m_price
        self.series_no = m_s_n

    def get_series_no(self):
        return self.series_no


if __name__ == '__main__':
    core_one = WatchCoreTypeOne("P001", 150, "KJ0042")
    band_one = WatchBandTypeOne("J001", 80, "BY1189")

    combine = AppleWatchBridge()
    combine.combine_watch(core_one, band_one)
    combine.show_version()
