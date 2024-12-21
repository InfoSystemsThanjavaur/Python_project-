"""
URL configuration for bug project.

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
        path('reg.html',views.reg,name='register'),
        path('userreg.html',views.ureg,name='userreg'),
        path('treg.html',views.treg,name='tester register'),
        path('dreg.html',views.dreg,name='developerregister'),
        path('assignbug.html',views.asignbug,name='assignbug'),
        path('user.html',views.user,name='userlogin'),
        path('tester.html',views.tester,name='tester'),
        path('developer.html',views.developer,name='developer'),
        path('viewdt.html',views.viewdt,name='view details'),
        path('udata.html',views.udata,name='user data'),
        path('ddata.html',views.ddata,name='developerdata'),
        path('tdata.html',views.tdata,name='tester data'),
        path('uprofile.html',views.upro,name='user profile'),
        path('addbug.html',views.addbug,name='add bug'),
        path('index.html',views.sample,name=''),
        path('viewbug.html',views.viewasg,name='view asg'),
        path('asgdev.html',views.asigndev,name="assign developer"),
        path('sndrpt.html',views.sndrpt,name='sendreport'),
        path('viewasgbug.html',views.viewasgbug,name='view assignbug'),
        path('viewslnad.html',views.viewslnad,name='view solution'),
        path('viewslnus.html',views.VIEWSLNUS,name='view solution'),
        path('addsln.html',views.addsln,name='add solution'),
]
