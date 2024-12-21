from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
   path('',views.sample,name=''),
   path('user.html',views.user,name='user'),
   path('register.html',views.reg,name='user'),
   path('user.html',views.user,name='user'),
   path('server.html',views.server,name='server'),
   path('views.html',views.viewsat,name='viewsatellite'),
   path('purchased.html',views.purchased,name='purchased'),
   path('upldel.html',views.upldel,name='upldel'),
   path('feedback.html',views.feedback,name='feedback'),
   path('analyser.html',views.analyser,name='analyser'),
   path('cntser.html',views.cntserver,name='cntserver'),
   path('behvior.html',views.behaviour,name='behavior'),
   path('products.html',views.products,name='products'),
   path('report.html',views.report,name='report'),
   path('vpurchased.html',views.vpurchased,name='vpurchased'),
   path('customer.html',views.customer,name='customer'),
   path('ordsat.html',views.ordsat,name='order satellite'),
   path('addpro.html',views.addproducts,name='addpro'),
   path('checkb.html',views.checkb,name='checkbehavior'),
   path('dailysales.html',views.dailys,name='dailysales'),
]
