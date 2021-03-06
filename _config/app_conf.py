#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import path

APP_DIR = path.abspath('.')

STATIC_DIR = path.join(APP_DIR, 'static')

CHERRYPY_CONFIG = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080,
    },
    '/': {
        'tools.staticdir.root': STATIC_DIR,
        'tools.sessions.on': True,
    },
    '/css': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'css',
    },
    '/img': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'img',
    },
    '/js': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'js',
    },
    '/task-check-86_files': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'landing/task-check-86_files',
    }
}
