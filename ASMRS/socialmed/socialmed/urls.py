"""
URL configuration for socialmed project.

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
    path('admin.html',views.sample1,name='admin'),
    path('reg.html',views.sample2,name='reg'),
    path('user.html',views.sample3,name='user'),
    path('addctg.html',views.addctc,name='add'),
    path('clrctg.html',views.clrctg,name='clear'),
    path('uplctg.html',views.uplctg,name='upload'),
    path('recomend.html',views.recom,name='recommend'),
    path('news.html',views.news,name='news'),
    path('postadd.html',views.post,name='post'),
    path('comment.html',views.com,name='comment'),
    path('viewact.html',views.view,name='view'),
    path('cmtsec.html',views.cmt1,name='comments'),
]
