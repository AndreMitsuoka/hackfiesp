#!/usr/bin/python
# -*- coding: utf-8 -*-
from model import user as User

class Person():
	def __init__(self, cpf,email,mobile_number):
		User(email,mobile_number)
		self.cpf = cpf
		createUser(self)