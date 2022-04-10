from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = " first name should be at least 2 characters"

        if len(postData['last_name']) < 2:
            errors["last_name"] = "last name should be at least 2 characters"
       
        if not EMAIL_REGEX.match(postData['email']):      
            errors['email'] = "Invalid email address!"
        
        if postData['password']  != postData['repassword']:
            errors['repassword'] = "password didn't matches!!"
        
        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters"

        return errors
    def login_validator(self, postData):
        errors1 = {}
        if len(postData['email']) < 1 or len(postData['passwordd'])<1 :
            errors1["login"] = " you must enter both password and email"
   
        return errors1

         
    

class User(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=150)
    objects=UserManager()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    

def register(info):
    password=info['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    User.objects.create(first_name=info['first_name'] ,last_name=info['last_name'] ,email=info['email'] ,password= pw_hash  )
def confermLogin(info):
    user = User.objects.get(email=info['email'])

    if user:
        if bcrypt.checkpw(info['passwordd'].encode(), user.password.encode()):
             return True
        else:
            return False
    else: 
        return False
