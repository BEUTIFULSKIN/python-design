#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-03 14:33:35
# @Author  : Yi Wang (gzytemail@126.com)
# @Link    : https://github.com/wang2222qq
# @des     : 桥接模式
"""
三个维度上建立桥接。
人 --> 车 --> 路
"""

# Abstract Road
class Road:
    def __init__(self):
        self._car_obj = None

    def run(self):
        pass

    def set_car_obj(self, value):
        self._car_obj = value

    def get_car_obj(self):
        return self._car_obj


class SpeedRoad(Road):
    def run(self):
        self._car_obj.run()
        print(u'高速公路上行驶')


class Street(Road):
    def run(self):
        self._car_obj.run()
        print(u'街道上行驶')


# Abstract Car
class AbstractCar:
    def __init__(self):
        self._human_obj = None

    def run(self):
        pass

    def set_human_obj(self, value):
        self._human_obj = value

    def get_human_obj(self):
        return self._human_obj


class Car(AbstractCar):
    def run(self):
        self._human_obj.drive()
        print(u'小汽车在')


class Bus(AbstractCar):
    def run(self):
        self._human_obj.drive()
        print(u'公交车在')


# Abstract Human
class Human:
    def drive(self):
        pass


class Male(Human):
    def drive(self):
        print(u"男人开着")


class Female(Human):
    def drive(self):
        print(u"女人开着")


def client():
    # 男人开着小汽车在高速公路上行驶
    road_obj = SpeedRoad()
    road_obj.set_car_obj(Car())
    road_obj.get_car_obj().set_human_obj(Male())
    road_obj.run()

    print("======")
    # 女人开着小汽车在街道上行驶
    road_obj = Street()
    road_obj.set_car_obj(Car())
    road_obj.get_car_obj().set_human_obj(Female())
    road_obj.run()

if __name__ == '__main__':
    client()