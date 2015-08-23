#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import requests
import redis
import re
import urlparse
import os

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

def createUser(self,user,interest = None):
    r.hset("user;"+user.email,"email", user.email)
    r.hset("user;"+user.email,"mobile_number", user.mobile_number)
    if interest is not None:
    	userInterest =""
    	for each in interest:
    		userInterest += each+";"
    	r.hset("user;"+user.email,"interest",userInterest)

def createProduct(product):
    r.hset("product;"+product.productName, "owner", product.userEmail)
    r.hset("product;"+product.productName, "name", product.productName)
    r.hset("product;"+product.productName, "expireDate", product.expireDate)
    r.hset("product;"+product.productName, "unity", product.unity)
    r.hset("product;"+product.productName, "price", product.price)
    r.hset("product;"+product.productName, "delivery", product.delivery)
    r.hset("product;"+product.productName, "category", product.categoria)

def getProducts():
    r.keys("product;*")
