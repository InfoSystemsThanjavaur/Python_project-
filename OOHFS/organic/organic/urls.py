
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.sample,name=''),
    path('admin.html',views.admin,name='admin'),
    path('ad2.html',views.ad2,name='admin2'),
    path('addp.html',views.addp,name='addproducts'),
    path('reg.html',views.reg,name='reg'),
    path('ureg.html',views.ureg,name='userreg'),
    path('sreg.html',views.sreg,name='sellerreg'),
    path('viewu.html',views.viewu,name='view user'),
    path('views.html',views.views,name='viewseller'),
    path('user.html',views.user,name='user'),
    path('seller.html',views.seller,name='seller'),
    path('selpro.html',views.selpro,name='profile'),
    path('addps.html',views.addps,name='addps'),
    path('viewsp.html',views.viewsp,name='viewssellerproduct'),
    path('logout.html',views.logout,name='logout'),
    path('logoutu.html',views.logoutu,name='logoutuser'),
    path('viewsselpr.html',views.viewsselpro,name='view seller products'),
    path('viewsupro.html',views.viewsupro,name='viewsuspro'),
    path('ordpro.html',views.order,name='order'),
    path('viewreq.html',views.viewreq,name='view request'),
    path('vieword.html',views.viewordu,name='view orders'),
    path('track.html',views.track,name='track order')
]
