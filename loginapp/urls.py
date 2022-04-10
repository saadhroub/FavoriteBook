from django.urls import path,include
from loginapp import views
urlpatterns = [
    path('',views.index),
    path('registration',views.registration),
    path('login',views.login)
]