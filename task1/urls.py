from django.urls import path
from task1 import views

urlpatterns=[path('', views.signup,name='signup'),
     path('signup', views.signup,name='signup'),
     path('login/signin', views.signin,name='signin'),
     path('signin', views.signin,name='signin'),
    ]