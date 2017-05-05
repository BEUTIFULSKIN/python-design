#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_stategy.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/4 17:37
#
#     描述  : 策略模式 —— 封装算法，由用户决定使用方式，常用于算法决策系统
#     例子  : 计算器，实现加减乘除


class Calculate:
    def __init__(self):
        self.operate = None

    def calcul(self, cal_str):
        if self.operate:
            re = cal_str.split(str(self.operate))


class PulsFunc(Calculate):
    def __init__(self):
        Calculate.__init__(self)
        self.operate = '+'

    def calcul(self, cal_str):
        re = cal_str.split(str(self.operate))
        rs = 0
        for num in re:
            rs += num
        return rs


class MinusFunc(Calculate):
    def __init__(self):
        Calculate.__init__(self)
        self.operate = '-'

    def calcul(self, cal_str):
        re = cal_str.split(str(self.operate))
        rs = 0
        for num in re:
            rs -= num
        return rs


class MultiplyFunc(Calculate):
    def __init__(self):
        Calculate.__init__(self)
        self.operate = '*'

    def calcul(self, cal_str):
        re = cal_str.split(str(self.operate))
        rs = 1
        for num in re:
            rs *= num
        return rs


class DivideFunc(Calculate):
    def __init__(self):
        Calculate.__init__(self)
        self.operate = '/'

    def calcul(self, cal_str):
        re = cal_str.split(str(self.operate))
        rs = 1
        for num in re:
            rs /= num
        return rs


class MixCalculate(Calculate):
    # 模拟计算器，计算整数的加减乘除
    def calcul(self, cal_str):
        result = 0
        re = cal_str.split('+')  # 复合算式 “1+2*3/4+6*5-8+1”
        if re:
            for item in re:
                # 判断划分之后的数是不是单个数，还是组合算式
                i_rs = set([str(item.split(x)) for x in ['-', '*', '/']])
                if len(i_rs) == 1:
                    result += float(item)
                else:
                    result += self.calculate_minus(item)
        else:
            result += self.calculate_minus(cal_str)
        print "result: ", result
        return result

    def calculate_minus(self, t_str):
        """
        funtion : 做含减法、乘法、除法的复合运算
        :param t_str:
        :return:
        """
        result = 0
        ree = t_str.split('-')
        if len(ree) == 1:  # 不存在减号,只剩下乘除，从左至右依次执行 “1*3/3*5”
            result += self.calculate_multiply_divide(t_str)
        else:  # “1*3-1*8-4”
            for e in ree:
                # 判断划分之后的数是不是单个数，还是组合算式
                i_rs = set([str(e.split(x)) for x in ['-', '*', '/']])
                if len(i_rs) == 1:
                    if ree.index(e) == 0:
                        result += float(e)
                    else:
                        result -= float(e)
                else:  # 不存在减号,只剩下乘除，从左至右依次执行 “1*3/3”
                    if ree[0] == e:  # 第一项是加项
                        result += self.calculate_multiply_divide(e)
                    else:  # 后面都是减项
                        result -= self.calculate_multiply_divide(e)
        return result

    def calculate_multiply_divide(self, t_str):
        """
        function : 仅仅只计算乘除的复合运算
        :param t_str:
        :return:
        """
        result = 1
        muti_index = 0
        divid_index = 0
        if '*' in t_str:
            muti_index = t_str.index('*')
        if '/' in t_str:
            divid_index = t_str.index('/')
        if muti_index and divid_index:  # 乘除法都存在
            if muti_index < divid_index:
                a, b = t_str.split('/')
                result = self.calculate_multiply_divide(a) / self.calculate_multiply_divide(b)
            elif muti_index < divid_index:
                a, b = t_str.split('*')
                result = self.calculate_multiply_divide(a) * self.calculate_multiply_divide(b)
        else:  # 只存在除法或者是乘法
            if muti_index:
                a, b = t_str.split('*')
                result = self.calculate_multiply_divide(a) * self.calculate_multiply_divide(b)
            elif divid_index:
                a, b = t_str.split('/')
                result = self.calculate_multiply_divide(a) / self.calculate_multiply_divide(b)
            else:
                result = float(t_str)
        return result

if __name__ == '__main__':
    calcul = MixCalculate()
    re = calcul.calcul("1+2*3/4+6*5-8+1.53")





