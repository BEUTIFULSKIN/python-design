#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-03 09:35:35
# @Author  : Yi Wang (gzytemail@126.com)
# @Link    : https://github.com/wang2222qq
# @des     : 适配器


class ConnectAdapter:
    """
	Adapts an object by replacing methods.
    Usage:
    engineer = Engineer()
    adapter = Adapter(engineer, connect=engineer.put_code)
    """
    def __init__(self, obj, **kw):
        self.obj = obj
        self.__dict__.update(kw)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


class Engineer:
    def __init__(self, name):
        self.name = name

    def put_code(self):
        print("Engineer:%s putting code!" % self.name)


class Student:
    def __init__(self, name):
        self.name = name

    def surf_internet(self):
        print("Student:%s Surfing the internet!" % self.name)

class Housewife():
    def __init__(self, name):
	   self.name = name

    def watch_tv(self):
        print("Housewife:%s Watching TV!" % self.name)

def client():
    objects = []
	# append object to container
    engineer = Engineer("Tom")
    objects.append(ConnectAdapter(engineer, connect=engineer.put_code))

    student = Student("Tina")
    objects.append(ConnectAdapter(student, connect=student.surf_internet))

    housewife = Housewife("Jina")
    objects.append(ConnectAdapter(housewife, connect=housewife.watch_tv))

	# run
    for obj in objects:
        obj.connect()


if __name__ == '__main__':
    client()
