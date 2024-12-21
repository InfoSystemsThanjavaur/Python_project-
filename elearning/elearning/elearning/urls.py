"""
URL configuration for elearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path('',views.sample,name=''),
   path('admin.html',views.admin,name='admin'),
   path('lrnadm.html',views.lrnadm,name='learning admission'),
   path('pmet.html',views.pmet,name='provide material'),
   path('learn.html',views.lrn,name='learner'),
   path('lrn.html',views.learn,name='learn'),
   path('ask.html',views.ask,name='ask query'),
   path('addfac.html',views.addfac,name='addfaculty'),
   path('faculty.html',views.faculty,name='faculty'),
   path('viewq.html',views.viewq,name='view question'),
   path('resans.html',views.resans,name='responsean'),
   path('logout.html',views.logout,name='logout'),
   path('recsln.html',views.recsln,name='recieve solution'),
]
 