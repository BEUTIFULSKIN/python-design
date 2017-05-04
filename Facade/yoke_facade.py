#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_facade.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/3 16:49
#
#     描述  : 外观模式，为管理子系统抽象出来的高层接口，显示给外界的统一接口
#
import time


class Drama:
    def __init__(self):
        self.content = u"话剧"

    def show_content(self):
        return self.content


class LifyShow:
    def __init__(self):
        self.content = u"生活剧"

    def show_content(self):
        return self.content


class DumbShow:
    def __init__(self):
        self.content = u"哑剧"

    def show_content(self):
        return self.content


# 演唱会
class Concert:
    def __init__(self):
        self.content = u"演唱会"

    def show_content(self):
        return self.content


# 舞台演出管理，针对观众的外观接口
class Stage:
    def __init__(self):
        self.show_list = []
        drama_show = Drama()
        self.show_list.append(drama_show)
        life_show = LifyShow()
        self.show_list.append(life_show)
        dumb_show = DumbShow()
        self.show_list.append(dumb_show)
        concert = Concert()
        self.show_list.append(concert)

    def show_time(self):
        for show_info in self.show_list:
            print show_info.show_content()
            time.sleep(1)
        print "Thanks for you watch!"


if __name__ == '__main__':
    stage_manage = Stage()
    stage_manage.show_time()
