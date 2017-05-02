#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-02 17:32:49
# @Author  : Yi Wang (gzytemail@126.com)
# @Link    : https://github.com/wang2222qq
# @des     : 线程安全单例模式

import threading

Lock = threading.Lock()

class SingleServer(object):
    _instance = None

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex 

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            try:
                Lock.acquire()   # double lock
                if not cls._instance:
                    cls._instance = super(SingleServer, cls).__new__(cls, *args, **kwargs)
                    print("create instance")
            finally:
                Lock.release()
        return cls._instance

    def printinfo(self):
        """ 
        打印参数
        """
        print("My name is %s" % self.name)
        print("I'm a %s" % self.sex)


def run(n, name, sex):
    single = SingleServer(name, sex)
    print("Treading_%d SingleServer id:%d" % (n, id(single)))
    single.printinfo()


def main():
    t1 = threading.Thread(target=run, args=(1, 'Test1', 'Male'))
    t2 = threading.Thread(target=run, args=(2, 'Test2', 'Female'))
    t3 = threading.Thread(target=run, args=(3, 'Test3', 'Male'))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("End")

if __name__ == "__main__":
    main()