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
#


# 学生
class Student:
    def __init__(self):
        self.u_sex = None
        self.u_age = None
        self.u_class = None
        self.u_dorm = None

    def set_age(self, t_age):
        if t_age:
            self.u_age = t_age

    def set_sex(self, t_sex):
        if t_sex:
            self.u_sex = t_sex

    def set_class(self, t_class):
        if t_class:
            self.u_class = t_class

    def set_dorm(self, t_dorm):
        if t_dorm:
            self.u_dorm = t_dorm

    def get_age(self):
        return self.u_age

    def get_sex(self):
        return self.u_sex

    def get_class(self):
        return self.u_class

    def get_dorm(self):
        return self.u_dorm

    def __str__(self):
        print "<Student info -- age: %s, sex: %s, classs: %s>" % \
              (self.u_age, self.u_sex, self.u_class)


# 划分处理类
class HandelRequest:
    def __init__(self):
        self.handel_obj = None  # 处理对象，可以是姓名，也可以是性别或其他

    # 年龄划分处理器
    def handel_by_age(self, t_student):
        self.handel_obj = t_student.get_age()
        if self.handel_obj>5 and self.handel_obj<=12:
            t_student.set_class("primary")
        elif self.handel_obj>12 and self.handel_obj<=14:
            t_student.set_class("junior high school")
        elif self.handel_obj>14 and self.handel_obj<=17:
            t_student.set_class("senior high school")
        elif self.handel_obj>17 and self.handel_obj<=21:
            t_student.set_class("college")

    # 性别划分处理器
    def handel_by_sex(self, t_student):
        self.handel_obj = t_student.get_sex()
        if self.handel_obj == 'girl':
            t_student.set_dorm("girl dorm")
        elif self.handel_obj == 'boy':
            t_student.set_dorm("boy dorm")


# 学生登记入口
class ChildSignUp:
    def __init__(self):
        self.student = None

    # 记录学生基本信息
    def recode_student_ino(self, t_sex, t_age):
        self.student = Student()
        self.student.set_sex(t_sex)
        self.student.set_age(t_age)

    # 根据年龄划分班级
    def divide_class(self):
        handel_obj = HandelRequest()
        handel_obj.handel_by_age(self.student)

    # 根据性别划分宿舍
    def divide_dorm(self):
        handel_obj = HandelRequest()
        handel_obj.handel_by_sex(self.student)

    # 展示学生完整信息
    def show_student_info(self):
        print self.student.get_age()
        print self.student.get_sex()
        print self.student.get_class()
        print self.student.get_dorm()

if __name__ == "__main__":
    print "#" * 40
    sign = ChildSignUp()
    sign.recode_student_ino('girl', 14)
    sign.divide_class()
    sign.divide_dorm()
    sign.show_student_info()
    print "#" * 40
    sign.recode_student_ino('boy', 19)
    sign.divide_class()
    sign.divide_dorm()
    sign.show_student_info()

