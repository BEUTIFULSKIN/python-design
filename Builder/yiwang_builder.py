#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-03 09:35:35
# @Author  : Yi Wang (gzytemail@126.com)
# @Link    : https://github.com/wang2222qq
# @des     : 创建者模式


class Director(object):
	def __init__(self):
		self._chef = None

	def construct_cooking(self):
		if self._chef:
			self._chef.new_cooking()
			self._chef.put_ingredients()
			self._chef.put_seasoning()

	def get_cooking(self):
		return self._chef.get_cooking()

	def set_chef(self, value):
		self._chef = value


# Abstruct Builder
class Chef(object):
	def __init__(self):
		self._cooking = None

	def new_cooking(self):
		self._cooking = Cooking()

	def get_cooking(self):
		return self._cooking


# Builder A
class PastryChef(Chef):
	def put_ingredients(self):
		self._cooking.set_ingredients(['egg', 'suger'])

	def put_seasoning(self):
		self._cooking.set_seasoning(['cherry', ])


# Builder B
class CantoneseCuisineChef(Chef):
	def put_ingredients(self):
		self._cooking.set_ingredients(['fish', ])

	def put_seasoning(self):
		self._cooking.set_seasoning(['ginger'])


# product
class Cooking(object):
	def __init__(self):
		self._ingredients = None
		self._seasoning = None

	def __repr__(self):
		return "ingredients:%s   \nseasoning:%s " % (self._ingredients, 
			                                         self._seasoning)		

	def set_ingredients(self, value):
		self._ingredients = value

	def set_seasoning(self, value):
		self._seasoning = value


# Client
if __name__ == '__main__':
	#Create derector
	direcotr = Director()

	# make pastry
	direcotr.set_chef(PastryChef())
	direcotr.construct_cooking()
	# show
	print(direcotr.get_cooking())

	# make cantonese cuisine
	direcotr.set_chef(CantoneseCuisineChef())
	direcotr.construct_cooking()

	# show
	print(direcotr.get_cooking())


