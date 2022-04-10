from django.urls import path,include
from app import views
urlpatterns = [
    path('mainpage',views.index),
    path('addfavbook/<int:userid>', views.addfavbook),
    path('addtofav/<int:userid>/<int:bookid>',views.addtofav),
    path('books/<int:bookid>',views.showbook),
    path('updatebook/<int:bookid>',views.updatebook),
    path('delete/<int:bookid>',views.deletebook),
    path('removefav/<int:userid>/<int:bookid>', views.removefav)


]