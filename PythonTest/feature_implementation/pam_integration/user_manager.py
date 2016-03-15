
from user import User


class UserManager:
    
    global user
    
    def __init__(self):
        user = User()
    
    
    def addUser(self):
        print 'add user'
        print user.username
    
    
    def modifyUser(self):
        print 'modify user'
        user.username = 'test_user'
        
        
    def deleteUser(self):
        print 'delete user'
        del user.username
        

userMgr = UserManager()
userMgr.addUser()
userMgr.modifyUser()
userMgr.addUser()
userMgr.deleteUser()
userMgr.addUser()

        
        
