#!/usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy
from _config import app_conf as config
from _config import secrets
from os import path
from jinja2 import Environment, FileSystemLoader
from cherrypy import request
from models import Person, Company , Product



env = Environment(loader = FileSystemLoader('static'))

class App(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('landing/task-check-86.html')
        return tmpl.render(title = 'Hello World!')

    @cherrypy.expose
    def cadastro(self):
        tmpl = env.get_template('cadastro.html')
        return tmpl.render(title ='Cadastro')

    @cherrypy.expose
    def cadastroProduto(self):
        tmpl = env.get_template('new_produto.html')
        return tmpl.render(title ='Cadastro de produto')

    @cherrypy.expose
    def createUserHandle(self,userId,idForUser,email,name,mobile,interests=None,onLogStatus=None):
        tmpl = env.get_template('produtos.html')

        if(userId == "cpf"):
            newUser = Person(idForUser,email,mobile,interests)
        else:
            newUser = Company(idForUser,email,mobile)

        productsList = Product.getProductsList()
        if productsList is None :
            productsList = []
        print onLogStatus
        return tmpl.render(products=productsList,title = 'Produtos Listados')

    @cherrypy.expose
    def createProductHandle(self, userId, productName, description, expireDate, unity, price, categoria, delivery=None):
        newProduct = Product(userId, productName, description, expireDate, unity, price, categoria, delivery)
        
        tmpl = env.get_template('produtos.html')
        productsList = Product.getProductsList()

        if productsList is None :
            productsList = []
        return tmpl.render(products=productsList,title = 'Produtos Listados')        

    @cherrypy.expose
    def produtos(self):
        tmpl = env.get_template('produtos.html')
        productsList = Product.getProductsList()
        if productsList is None :
            productsList = []
        return tmpl.render(products=productsList,title = 'Produtos Listados')

    @cherrypy.expose
    def login(self):
        tmpl = env.get_template('login.html')
        return tmpl.render(title = 'Realimente')


cherrypy.quickstart(App(), '/', config.CHERRYPY_CONFIG)
