#!/usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy
from _config import app_conf as config
from _config import secrets
from os import path
from jinja2 import Environment, FileSystemLoader
from cherrypy import request
from models import Person, Company




env = Environment(loader = FileSystemLoader('static'))

class App(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render(title = 'Hello World!')

    @cherrypy.expose
    def cadastro(self):
    	tmpl = env.get_template('cadastro.html')
    	return tmpl.render(title ='Cadastro')

    @cherrypy.expose
    def createUserHandle(self,userId,idForUser,email,name,mobile):
    	if(userId == "cpf"):
    		newUser = Person(idForUser,email,mobile)
    	else:
    		newUser = Company(idForUser,email,mobile)
    	return ""





cherrypy.quickstart(App(), '/', config.CHERRYPY_CONFIG)
