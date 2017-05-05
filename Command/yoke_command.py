#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_command.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/5 17:47
#
#     描述  : 命令模式 —— 将一个请求封装成对象，从而可以使用不同的请求对用户进行参数化
#                           对请求排队、记录请求日志和撤销操作；
#
import os


class MoveFileCommand(object):
    def __init__(self, t_src, t_dest):
        self.src = t_src
        self.dest = t_dest

    def excute(self):
        self()

    def __call__(self):
        print "{} to rename {}".format(self.src, self.dest)
        path = os.getcwd()
        os.rename(path+self.src, path+self.dest)

    def undo(self):
        path = os.getcwd()
        os.rename(path+self.dest, path+self.src)


if __name__ == '__main__':
    move_list = []
    move_list.append(MoveFileCommand("a2017.txt", "b2017.txt"))
    move_list.append(MoveFileCommand("b2017.txt", "c2017.txt"))

    for item in move_list:
        item.excute()

    for item in reversed(move_list):
        item.undo()