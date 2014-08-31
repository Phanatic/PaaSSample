#!/usr/bin/env python

import re
import os
import sys
import time
import bottle
import logging
import urllib2
import urlparse
import contextlib

from bottle import route, request,get, post, put, delete, response

from users import User
from users import UserDb
from users import UserEncoder

import json

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')


logging.basicConfig()
log = logging.getLogger('paas-sample')
log.setLevel(logging.DEBUG)

mysql_url = os.environ['MYSQL_URL']

dbname = os.environ['DBNAME']
user = os.environ['USER']
password = os.environ['PASSWORD']
#rdb = redis.Redis(host=url.hostname, port=url.port, password=url.password)

userDb = UserDb(mysql_url,dbname,user,password)

'''
service routes
'''

@post('/adduser')
def adduser():
    
    fname = request.forms['fname']
    lname = request.forms['lname']
    email = request.forms['email']
    
    user = User(fname=fname,lname=lname,email=email )
    addedUser = userDb.addUser(user)
    return json.dumps(addedUser.__dict__)

@delete('/deleteuser/:id')

def deleteuser(id):
    userDb.removeUserById(id)
    response.status = 201
 
@get('/getusers') 
def getusers():
    users = userDb.getAllUsers()
    
    return json.dumps(users,cls=UserEncoder)

@put('/updateuser/:reqid')
def updateuser(reqid):
    fname = request.forms['fname']
    lname = request.forms['lname']
    email = request.forms['email']
    
    user = User(id = reqid,fname=fname,lname=lname,email=email )
    
    userDb.updateUser(user)
    response.status = 201
'''
view routes
'''

@route('/')
def home():
    return bottle.template('home')

@route('/static/:filename')
def serve_static(filename):
    return bottle.static_file(filename, root=STATIC_ROOT)


'''
service runner code
'''
application = bottle.app()
application.catchall = False

url = urlparse.urlparse(os.environ['URL'])
port = int(os.getenv('PORT'))
bottle.run(application, host=url, port=port)

