#!/usr/bin/python
# -*- coding: utf-8 -*-
from DAL import userDB 

class Company():
    def __init__(self, cnpj,email,mobile_number):
        self.user = User(email,mobile_number)
        self.cnpj = cnpj
        userDB.createUser(self,self.user)

class Person():
    def __init__(self, cpf,email,mobile_number,interests):
        self.user = User(email,mobile_number)
        self.cpf = cpf
        self.interests = interests
        if interests is not None:
            print interests
        userDB.createUser(self,self.user,interests)

class Product:
    def __init__(self, owner,productName,desc, date, unity, price, categoria, delivery = False):
        self.userEmail = owner
        self.productName = productName
        self.description = desc
        self.expireDate = date
        self.unity = unity
        self.price = price
        self.delivery = delivery
        self.categoria = categoria
        userDB.createProduct(self)

    @staticmethod
    def getProductsList():
        return userDB.getProducts()

class User:
    def __init__(self,email,mobile_number):
        self.email = email
        self.mobile_number = mobile_number