'''
Created on Aug 29, 2014

@author: jacoba
'''
import unittest
from users import UserDb
from users import User
import json
from users import UserEncoder

class Test(unittest.TestCase):

    def setUp(self):
        try:
            userDb = UserDb('localhost','paassample','user1','user1')
            user = User(fname='John',lname='Doe',email='john.doe@foo.com')
            userDb.addUser(user)
        except Exception as e: 
            self.fail('exception thrown in setup = %s'%str(e))
            


    def tearDown(self):
        try:
            userDb = UserDb('localhost','paassample','user1','user1')
            users = userDb.getUsersByField('user_fname','John')
            
            if(users != None):
                if(len(users) == 1):
                    user = users[0]
                    userDb.removeUser(user)
                
        except Exception as e: 
            self.fail('exception thrown in setup = %s'%str(e))
            
    
    
    def testQueryByFName(self):
        '''
        this method assumes you've got a localhost db, a user1/user1 configured user, and a cfpaassample database.
        in that database, it assumes youve got a row where user_fname = John and user_lname = Doe
        you should have those if you ran the local sql scripts. 
        '''
        
        try:
            userDb = UserDb('localhost','paassample','user1','user1')
            
            users = userDb.getUsersByField('user_fname','John')
            
            self.assertTrue(users != None)
            
            self.assertEqual(1,len(users))
            user = users[0]
            
            self.assertEqual('John',user.fname)
        except Exception as e: 
            self.fail('exception thrown in test = %s'%str(e))
        
        
    def testQueryByLName(self):
        '''
        this method assumes you've got a localhost db, a user1/user1 configured user, and a cfpaassample database.
        in that database, it assumes youve got a row where user_fname = John and user_lname = Doe
        you should have those if you ran the local sql scripts. 
        '''
        
        try:
            userDb = UserDb('localhost','paassample','user1','user1')
            
            users = userDb.getUsersByField('user_lname','Doe')
            
            self.assertTrue(users != None)
            
            self.assertEqual(1,len(users))
            user = users[0]
            
            self.assertEqual('John',user.fname)
        except Exception as e: 
            failure = 'exception thrown in test = %s'%str(e)
            self.fail(failure)

    def testAddAndRemoveUser(self):
        try:
            userDb = UserDb('localhost','paassample','user1','user1')
            
            user = User( fname = 'Jane', lname = 'Doe', email = 'jane.doe@foo.bar')
            
            userAdd = userDb.addUser(user)
            
            self.assertTrue(userAdd != None)
            self.assertTrue(userAdd.id != None)
            
            users = userDb.getUsersByField('user_lname','Doe')
            
            self.assertTrue(users != None)
            
            self.assertEqual(2,len(users))
            
            # todo: find Jane and remove her. 
            
            userJane = None
            for user in users: 
                if user.fname == 'Jane':
                    userJane = user
                    break;
                
            self.assertTrue(userJane != None)
            
            passed = userDb.removeUser(userJane)
            
            self.assertTrue(passed)
            
        except Exception as e: 
            self.fail('exception thrown in test = %s'%str(e))
            
    def testEditUser(self):
        try:
            userDb = UserDb('localhost','paassample','user1','user1')
        
            users = userDb.getUsersByField('user_fname','John')
            
            self.assertEquals(1,len(users))
            
            user = users[0]
            user.lname = "Smith"
            
            userDb.updateUser(user)
            user.lname = "Doe"
            userDb.updateUser(user)
            
        except Exception as e: 
            self.fail('exception thrown in test = %s'%str(e))
            
    def testGetAllUsers(self):
        try:
            userDb = UserDb('localhost','paassample','user1','user1')
            users = userDb.getAllUsers()
            self.assertFalse(None == users)
        except Exception as e: 
            self.fail('exception thrown in test = %s'%str(e))

    def testJSONDumpAllUsers(self):
        try:
            userDb = UserDb('localhost','paassample','user1','user1')
            users = userDb.getAllUsers()
            self.assertFalse(None == users)
            
            txt = json.dumps(users,cls=UserEncoder)
            print txt
        except Exception as e: 
            self.fail('exception thrown in test = %s'%str(e))
    
    def testRemoveUserById(self):
        try:
            userDb = UserDb('localhost','paassample','user1','user1')
            users = userDb.getUsersByField('user_fname','John')
            user = users[0]
            removed = userDb.removeUserById(user.id)
            self.assertTrue(removed)
        except Exception as e: 
            self.fail('exception thrown in test = %s'%str(e))
            
#    def testRemoveUserById(self):
#        try:
#            
#            
#            userDb = Users('localhost','paassample','user1','user1')
#            user = User(None, fname = 'Jane', lname = 'Doe', email = 'jane.doe@foo.bar')
#            
#            print user.fname
#            userAdd = userDb.addUser(user)
#            
#            userDb.removeUserById(userAdd.id)
#            
#            Users = userDb.getUsersByField("id",id)
#            
#        except Exception as e: 
#            self.fail('exception thrown in test = %s'%str(e))
    
        
            
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testQueryByField']
    unittest.main()
    