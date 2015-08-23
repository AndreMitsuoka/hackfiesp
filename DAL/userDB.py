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
	r.hset(user.email,"email",user.email)
	r.hset(user.email,"phone",user.mobile_number)