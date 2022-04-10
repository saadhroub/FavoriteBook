from django.shortcuts import render,redirect
from app.models import User,Book
from app import models
from django.contrib import messages

def index(request):
    context={
        'user':User.objects.get(email=request.session['email']),
        'books':Book.objects.all()
    }
    return render(request,'mainPage.html',context)
def addfavbook(request,userid):
    errors2 = Book.objects.registration_validator(request.POST)
        
    if len(errors2) > 0:
        context={
        'user':User.objects.get(email=request.session['email']),
        'books':Book.objects.all()
    }
       
       
        for key, value in errors2.items():
            messages.error(request, value)
       
        return render(request, 'mainpage.html',context)
    else:
        models.addfavbook(request.POST,userid)
        return redirect('/mainpage')
def addtofav(request,userid,bookid):
    models.addtofavv(userid,bookid)
    return redirect('/mainpage')
def showbook(request,bookid):
    book= Book.objects.get(id=bookid)
    user= User.objects.get(email=request.session['email'])
    context={
        'user':User.objects.get(email=request.session['email']),
        'book': book
    }
    if book in user.books_uploaded.all():
        
        return render(request,'mybook.html',context)
    else :
        return render(request,'otherbook.html',context)
def updatebook(request,bookid):
    book=Book.objects.get(id=bookid)
    book.desc=request.POST['desc']
    book.save()
    return redirect('/mainpage')
def deletebook(request,bookid):
    book=Book.objects.get(id=bookid)
    book.delete()
    return redirect('/mainpage')
def removefav(request,userid,bookid):
    book=Book.objects.get(id=bookid)
    user=User.objects.get(id=userid)
    user.liked_books.remove(book)
    return redirect('/mainpage')

        
        
