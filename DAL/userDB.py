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

def createUser(self,user):
	r.hset("user;"+user.email,user.email,user.mobile_number)

def createProduct(self,product):
	r.hset("product;"+product.name, userEmail,productName,expireDate,unity,price,delivery)

def getProducts():
	r.keys("products;")