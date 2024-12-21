from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
   path('',views.sample,name=''),
   path('admin.html',views.admin,name='admin'),
   path('user.html',views.user,name='user'),
   path('reg.html',views.register,name='register'),
   path('condt.html',views.condt,name='condt'),
   path('medicine.html',views.medicine,name='medicine'),
   path('clrprod.html',views.clrpro,name='clrpro'),
   path('profile.html',views.profile,name='profile'),
   path('meddt.html',views.meddt,name='meddt'),
   path('logout.html',views.logout,name='logout'),
   path('feedback.html',views.fedback,name='feedback'),
   path('hospital.html',views.hospital,name='hospital'),
   path('cntus.html',views.cntus,name='contactus'),
   path('hlogout.html',views.hlogout,name='hlogout'),
   path('clrstack.html',views.clrstck,name='clear stack'),
   path('viewdt.html',views.hviews,name='hviews'),
   path('views.html',views.aviews,name='views'),

]