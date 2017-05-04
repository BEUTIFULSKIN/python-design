#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-04 11:25:15
# @Author  : Yi Wang (gzytemail@126.com)
# @Link    : https://github.com/wang2222qq
# @des     : 享元模式
import weakref 
 
 
class Card(object):
    """The object pool. Has builtin reference counting"""
    _CardPool = weakref.WeakValueDictionary()
 
    """Flyweight implementation. If the object exists in the
    pool just return it (instead of creating a new one)"""
    def __new__(cls, value, suit):        
        obj = Card._CardPool.get(value + suit, None)        
        if not obj:            
            obj = object.__new__(cls)            
            Card._CardPool[value + suit] = obj            
            obj.value, obj.suit = value, suit      
        return obj
 
    def __repr__(self):        
        return "<Card: %s%s %s>" % (self.value, self.suit, hex(id(self)))     
 
 
if __name__ == '__main__':
    # comment __new__ and uncomment __init__ to see the difference
    c1 = Card('1', 'h')
    c2 = Card('2', 'h')
    c3 = Card('3', 'h')
    print("c1:", c1)
    print("c2:", c2)
    print("c3:", c3)
    # del c1, c2, c3
    c4 = Card('1', 'h')
    c5 = Card('2', 'h')
    c6 = Card('3', 'h')
    print("c4:", c4)
    print("c5:", c5)
    print("c6:", c6)


