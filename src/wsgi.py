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

from bottle import route, request,get, post, put, delete, response, template

from users import User
from users import UserDb
from users import UserEncoder

import json

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')


logging.basicConfig()
log = logging.getLogger('paas-sample')
log.setLevel(logging.DEBUG)



mysql_url = urlparse.urlparse(os.environ['MYSQL_URL'])

print os.environ['MYSQL_URL']
#rdb = redis.Redis(host=url.hostname, port=url.port, password=url.password)

url = mysql_url.hostname
password = mysql_url.password
user = mysql_url.username
dbname = mysql_url.path[1:] # slice off the '/'

#user = os.environ['USER']
#password = os.environ['PASSWORD']
##rdb = redis.Redis(host=url.hostname, port=url.port, password=url.password)

userDb = UserDb(url,dbname,user,password)

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

@delete('/deleteuser/:userid')

def deleteuser(userid):
    userDb.removeUserById(userid)
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

@route('/userForm/:action')
def userForm(action):
    if action == 'add':
        return template('user.tpl',action='add',fname=None,lname=None,email=None) 
    elif action == 'edit':
        userid = request.GET['userid']
        user = userDb.getUserById(userid)
        return template('user.tpl',action='edit', userid=userid,fname=user.fname,lname=user.lname,email=user.email)
        

@route('/static/:filename')
def serve_static(filename):
    return bottle.static_file(filename, root=STATIC_ROOT)


'''
service runner code
'''
application = bottle.app()
application.catchall = False

#if os.getenv('SELFHOST', False):
#UNCOMMENT BEFORE RUNNING ON CLOUD
url = os.getenv('VCAP_APP_HOST')
port = int(os.getenv('VCAP_APP_PORT'))
bottle.run(application, host=url, port=port)

