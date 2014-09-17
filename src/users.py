'''
Created on Aug 29, 2014

@author: jacoba
'''
import MySQLdb
import json

class User():
    def __init__(self,row = None,id = None, fname = None, lname = None, email = None):
        # if there are 4 values in tuple, assume this is being filled from a query
        
        if row != None and len(row) == 4: 
            self.id = int(row[0])
            self.fname = row[1]
            self.lname = row[2]
            self.email = row[3]
        else:
            if id != None:
                self.id = int(id)
            self.fname = fname
            self.lname = lname
            self.email = email
        
class UserEncoder(json.JSONEncoder):
    
    def default(self,o):
        return o.__dict__
    
    
class UserDb:
    def handleMySQLException(self,e,throwEx=False):
        try:
            print "Error [%d]: %s"%(e.args[0],e.args[1])
        except IndexError:
            print "Error: %s"%str(e)
            
        raise e
            
            
    def __init__(self,url,dbName,userName,password):
        try:
            self.db = MySQLdb.connect(host=url,user=userName,passwd=password,db=dbName)
            cur = self.db.cursor()
            cur.execute('use %s'%dbName)
        except MySQLdb.Error, e:
            self.handleMySQLException(e,True)
    
    def getUserById(self,userId):
        try:
            
            cur = self.db.cursor()
            cur.execute("select user_id, user_fname, user_lname, user_email from users where user_id=%s"%userId)
            rows = cur.fetchall()
            user = User(rows[0])
            return user
        except MySQLdb.Error, e:
            self.handleMySQLException(e)
        
    def getByRawQuery(self,query):
        users = []
        try:
            
            cur = self.db.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            return rows
            
        except MySQLdb.Error, e:
            self.handleMySQLException(e)
            
            
        
        
    def getUsersByField(self,fieldName,fieldTerm):
        users = []
        try:
            query = 'select user_id,user_fname,user_lname,user_email from users where %s = '%fieldName
            query = query + '%s'
            cur = self.db.cursor()
            cur.execute(query,(fieldTerm))
            rows = cur.fetchall()
            
            
            for row in rows:
                users.append(User(row))
            
            
        except MySQLdb.Error, e:
            self.handleMySQLException(e)
            users = None
            
        return users

    def addUser(self,user):
        fullUser = None
        try:
            query = 'insert into users(user_fname,user_lname,user_email) values(%s,%s,%s)'
            cur = self.db.cursor()
            cur.execute(query,(user.fname,user.lname,user.email))
            self.db.commit()
            rawQ = "select user_id from users where user_fname='%s' and user_lname='%s' and user_email='%s'"%(user.fname,user.lname,user.email)
            rows = self.getByRawQuery(rawQ)
            row = rows[0]
            userId = int(row[0])
            fullUser = User(None,id=userId,fname = user.fname,lname = user.lname,email = user.email)
            
        except MySQLdb.Error as e:
            print str(e)
            self.handleMySQLException(e)
            
        return fullUser
    
    def removeUserById(self,id):
        try:
            query = 'delete  from users where user_id=%s'
            cur = self.db.cursor()
            cur.execute(query,(id))
            self.db.commit()
            return True
        except MySQLdb.Error, e:
            self.handleMySQLException(e)
            return False
    def removeUser(self,user):
        try:
            query = 'delete  from users where user_fname=%s and user_lname=%s and user_email=%s'
            cur = self.db.cursor()
            cur.execute(query,(user.fname,user.lname,user.email))
            self.db.commit()
            return True
        except MySQLdb.Error, e:
            self.handleMySQLException(e)
            return False
        
    def updateUser(self,user):
        try:
            query = 'update users set user_fname=%s, user_lname=%s, user_email=%s where user_id=%s'
            cur = self.db.cursor()
            cur.execute(query,(user.fname,user.lname,user.email,user.id))
            self.db.commit()
            return True
        except MySQLdb.Error, e:
            self.handleMySQLException(e)
            return False
    
    def getAllUsers(self):
        users = []
        
        try:
            query = 'select user_id,user_fname,user_lname,user_email from users'
            cur = self.db.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            
            for row in rows:
                users.append(User(row))
        except MySQLdb.Error, e:
            self.handleMySQLException(e)
            
        return users
    
if __name__ == '__main__':
    pass