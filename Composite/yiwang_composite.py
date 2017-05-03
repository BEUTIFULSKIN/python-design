#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-03 16:00:12
# @Author  : Yi Wang (gzytemail@126.com)
# @Link    : https://github.com/wang2222qq
# @des     : 组合模式 
#            主要用于树型结构让你可以优化处理递归或分级数据结构


class Material:
    def __init__(self, code):
        self.code = code

    def add(self, material_obj):
        pass

    def remove(code):
        pass

    def get_composite(self, level):
        pass


class RawMaterial(Material):
    def add(self, material_obj):
        raise SyntaxError("RawMaterial can't add material_obj")

    def get_composite(self, level):
        strtemp = "-" * level
        strtemp += self.code
        print strtemp


class Bom(Material):
    def __init__(self, code):
        self.code = code
        self._compisite = []

    def add(self, material_obj):
        self._compisite.append({'code': material_obj.code,
                                'obj': material_obj})

    def remove(code):
        for index, item in enumerate(self._compisite):
            if code == item['code']:
                self._compisite.remove(index)
                print("remove raw material:%s from bom:%s OK" % (code, self.code))
                break

    def get_composite(self, level):
        strtemp = "-" * level
        strtemp += self.code
        print strtemp
        for item in self._compisite:
            item['obj'].get_composite(level + 2)


def client():
    bom = Bom('BOM00001')
    bom.add(RawMaterial(u'螺丝钉'))
    bom.add(RawMaterial(u'螺母'))
    bom2 = Bom('BOM00002')
    bom2.add(RawMaterial(u'乳胶'))
    bom.add(bom2)
    bom.get_composite(1)


if __name__ == '__main__':
    client()