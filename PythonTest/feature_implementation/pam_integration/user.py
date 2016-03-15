
from user_constants import UserConstants

class User:
    
    username = 1
    password = 2
    
    def __init__(self):
        self._username = UserConstants.DEFAULT_USERNAME
        self._password = UserConstants.DEFAULT_PASSWORD  
        self.group = UserConstants.DEFAULT_GROUP
    
    @property
    def get_username(self):
        return self.username
    
    @username.setter
    def set_username(self, name):
        self.username = name
        
        
    @property
    def get_password(self):
        return self.password
    
    @password.setter
    def set_password(self, passwd):
        self.username = passwd
