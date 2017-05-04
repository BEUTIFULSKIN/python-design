#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_compsite.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/3 16:51
#
#     描述  : 组合模式 —— 用于目录结构，是部分 + 整体，部分整体都可对外对立调用
#


class Composite:
    def __init__(self):
        self.index = None
        self.level = 0
        self.t_next = None

    def add(self, node):  # 添加节点
        pass

    def remove(self, node):  # 移除节点
        pass

    def traverse(self):  # 遍历
        pass

    def get_level(self):
        return self.level

    def get_next_node(self):
        return self.t_next


class NodeLeaf(Composite):
    def __init__(self, t_index):
        Composite.__init__(self)
        self.index = t_index

    def add(self, node):
        print "this is leaf node, can not add"

    def traverse(self):
        print "index: {}, level: {}".format(self.index, self.level)


class NodeComposite(Composite):
    def __init__(self, t_index):
        Composite.__init__(self)
        self.index = t_index

    def add(self, node):
        if not self.t_next:
            self.t_next = node
            self.level = self.t_next.get_level() + 1
        else:
            print "already exist next node, if you continue add will be replace next node"

    def traverse(self):
        if self.t_next:
            print "index: {}, level: {}".format(self.index, self.level)
            self.t_next.traverse()

if __name__ == "__main__":
    leaf_1 = NodeLeaf('001')
    c_node_1 = NodeComposite('101')
    c_node_1.add(leaf_1)
    leaf_2 = NodeLeaf('002')
    c_node_2 = NodeComposite('102')
    c_node_2.add(c_node_1)
    c_node_3 = NodeComposite('103')
    c_node_3.add(c_node_2)
    c_node_3.traverse()
    leaf_2.add(leaf_1)
    leaf_2.traverse()






