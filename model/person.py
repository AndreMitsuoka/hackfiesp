#!/usr/bin/python
# -*- coding: utf-8 -*-

class Person(User):
	def _init(self, cpf,email,mobile_number):
		User._init_(email,mobile_number)
		self.cpf = cpf