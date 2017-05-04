#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-04 11:12:56
# @Author  : Yi Wang (gzytemail@126.com)
# @Link    : https://github.com/wang2222qq
# @des     : 外观模式


class SubSystemA:
    """
    子系统A
    """
    def run(self):
        print("运行子系统A")


class SubSystemB:
    def method(self):
        print("运行子系统B")


class SubSystemC:
    def run(self):
        print("运行子系统C")


class Facade:
    def run(self, m_type):
        if m_type == 0:
            obj = SubSystemA()
            obj.run()
        elif m_type == 1:
            obj = SubSystemB()
            obj.method()
        else:
            obj = SubSystemC()
            obj.run()


if __name__ == '__main__':
    facade = Facade()
    facade.run(0)
    facade.run(1)
    facade.run(2)
        