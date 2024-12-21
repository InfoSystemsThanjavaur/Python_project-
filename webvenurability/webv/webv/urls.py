
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.sample,name=''),
    path('reg.html',views.register,name='register'),
    path('user.html',views.std,name='studentlogin'),
    path('sndapp.html',views.sndapp,name='sendapplication'),
    path('management.html',views.man,name='manufactured'),
    path('addc.html',views.addc,name='add comapany'),
    path('delcmpy.html',views.delcmpy,name='delcompany'),
    path('viewcmp.html',views.viewcmpy,name='view company'),
    path('viewapp.html',views.viewapp,name='viewapplication'),
    path('company.html',views.cmpy,name='company'),
    path('placement.html',views.place,name='placement'),
    path('sndrep.html',views.sndrep,name='report'),
    path('viewstu.html',views.viewstu,name='views students'),
    path('viewgen.html',views.viewgen,name='generate report'),
    path('viewplace.html',views.viewplace,name='placement'),
    path('test.html',views.test,name='test'),

]
