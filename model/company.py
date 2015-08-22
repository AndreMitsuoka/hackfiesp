#!/usr/bin/python
# -*- coding: utf-8 -*-

class Company(User):
	def _init_(self, cnpj,email,mobile_number):
		User._init_(email,mobile_number)
		self.cnpj = cnpj