import re
from tkinter import CASCADE
from django.db import models
from loginapp.models import User
class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        
        if len(postData['title']) < 2:
            errors["title"] = " title must be at least 2 litters"

        if len(postData['desc']) < 5:
            errors["last_name"] = "Description must be at least 5 litters"
       
       

        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    users_who_likes=models.ManyToManyField(User,related_name='liked_books')
    uploaded_py=models.ForeignKey(User,related_name='books_uploaded', on_delete=CASCADE)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
def addfavbook(info,userid):
    
    Book.objects.create(title=info['title'],uploaded_py=User.objects.get(id=userid),desc=info['desc'])
    book=Book.objects.last()
    user=User.objects.get(id=userid)
    user.liked_books.add(book)

    return
def addtofavv(userid,bookid):
    book=Book.objects.get(id=bookid)
    user=User.objects.get(id=userid)
    user.liked_books.add(book)
    return


