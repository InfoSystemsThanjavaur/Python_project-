
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name=''),
    path('reg.html',views.reg,name='register'),
    path('user.html',views.user,name='userlogin'),
    path('profile.html',views.profile,name='view profile'),
    path('req.html',views.req,name='reqeust to cloud'),
    path('comment.html',views.cmt,name='comments'),
    path('cloudserver.html',views.cloud,name='name'),
    path('deluser.html',views.deluser,name='deluser'),
    path('rply.html',views.rply,name='name'),
    #path('dynsch.html',views.dynsch,name='dynamic'),
    path('clogin.html',views.clogin,name='clogin'),
    path('setsch.html',views.setsch,name='setscheduling'),
    path('index.html',views.logout,name='logout'),
    path('viewsch.html',views.viewsch,name='set scheduling'),
    path('viewreq.html',views.viewreq,name='view request'),
    path('loadbalancer.html',views.load,name='load'),
    path('upldt.html',views.upldt,name='upldata'),
    path('viewdata.html',views.viewdata,name='view data'),
    path('dynlogin.html',views.dynlogin,name='dynlogin')
]
