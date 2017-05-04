#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-04 15:00:56
# @Author  : Yi Wang (gzytemail@126.com)
# @Link    : https://github.com/wang2222qq
# @des     : 责任链模式


class Handle:
    def successor(self, excption_obj):
        self.dealer = excption_obj


class DealHandle1(Handle):
    def handle(self, code):
        if code >= 100 and code < 200:
            print("exception deal by DealHandle1")
        else:
            self.dealer.handle(code)


class DealHandle2(Handle):
    def handle(self, code):
        if code >= 200 and code < 300:
            print("exception deal by DealHandle2")
        else:
            self.dealer.handle(code)


class DealHandle3(Handle):
    def handle(self, code):
        if code >= 300 and code < 400:
            print("exception deal by DealHandle3")
        else:
            print("end chain. no handle for {}".format(code))


def client():
    h1 = DealHandle1()
    h2 = DealHandle2()
    h3 = DealHandle3()

    h1.successor(h2)
    h2.successor(h3)

    exception_code_list = [20, 100, 130, 200, 300, 305, 502]
    for exception_code in exception_code_list:
        h1.handle(exception_code)


if __name__ == '__main__':
    client()