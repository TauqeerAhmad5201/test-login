from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.index, name='index'),
    path('account', views.join, name='join'),
    path('signup',views.signup,name='signup'),
    path('signupsent',views.signupsent,name='signupsent'),
    path('loginsent', views.loginsent, name='loginsent')
]