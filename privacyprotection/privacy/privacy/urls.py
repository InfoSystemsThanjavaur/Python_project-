
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.sample,{}),
    path('reg.html',views.reg,{}),
    path('patient.html',views.plogin,name='patientlogin'),
    path('patient2.html',views.patient,name='patient'),
    path('sndap.html',views.sndap,name='sendapplication'),
    path('logoutp.html',views.logout,name='logout'),
    path('doctor.html',views.doctor,name='doctorlogin'),
    path('doctor2.html',views.dct2,name='doctor2'),
    path('prq.html',views.prq,name='patientrequiest'),
    path('pinfo.html',views.pinfo,name='patientinfo'),
    path('hreport.html',views.hreport,name='hreport'),
    path('prescripd.html',views.presc,name='prescription'),
    path('rqfdc.html',views.rqfdct,name='requestfromdct'),
    path('prescriptionp.html',views.prescriptp,name='prescriptionp'),
    path('cloudlet.html',views.cloudlet,name='cloudlet'),
    path('doctorreg.html',views.adddct,name='doctordetails'),
    path('doctorinfo.html',views.dctinfo,name='view doctor'),
    path('viewpat.html',views.pinfocloud,name='pinfocloud'),
    path('intruder.html',views.intruder,name='intruder'),
    path('change.html',views.change,name='change'),
    path('intruderc.html',views.intrudc,name='intrudercloud')
]
