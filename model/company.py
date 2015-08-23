#!/usr/bin/python
# -*- coding: utf-8 -*-
from model import user as User

class Company():
    def __init__(self, cnpj,email,mobile_number):
        User(email,mobile_number)
        self.cnpj = cnpj
        createUser(self)