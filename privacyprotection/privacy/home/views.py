from django.shortcuts import render
import mysql.connector
def sample(request):
    return render(request,'index.html',{})



def reg(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
            reg7 = request.POST['r7']
            reg8 = request.POST['r8']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 or len(reg7)==0 or len(reg8)==0 :
                return render(request,'reg.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
                mycursor=mydb.cursor()
                sql="insert into patient (name,age,mobile,email,password,gender,dept,date)values(%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,reg7,reg8,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'reg.html',{'result':'register succesfully!..'})
    else:
         return render(request,'reg.html',{'result':'registration page'})

def plogin(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
        mycursor=mydb.cursor()
        sql="select name ,password from patient where  name = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'patient2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'patient.html',{'result':'failure'})

    else:
        return render(request,'patient.html',{'result':'registration page!!'})
def patient(request):
    return render(request,'patient2.html',{})
def sndap(request):
    return render(request,'sndap.html',{})

def sndap(request):
    if request.method == "POST":
            po1 = request.POST['p1']
            po2 = request.POST['p2']
            po3 = request.POST['p3']
            po4 = request.POST['p4']
            po5 = request.POST['p5']
            po6 = request.POST['p6']
          
            if len(po1)== 0 or len(po2)==0 or len(po3)==0 or len(po4)==0 or len(po5)==0 or len(po6)==0 :
                return render(request,'sndap.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
                mycursor=mydb.cursor()
                sql="insert into sndapp(name,dept,age,gender,status,date)values(%s,%s,%s,%s,%s,%s)"
                val=(po1,po2,po3,po4,po5,po6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'sndap.html',{'result':'appointment send succesfully!.'})
    else:
         return render(request,'sndap.html',{'result':'appointmentpage!.'})

def logout(request):
    if request.method=='POST':
        del1=request.POST['c1']
        del2=request.POST['c2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
        mycursor=mydb.cursor()
        sql1='delete from patient where name =(%s) and email =(%s)'
        val2=(del1,del2,)
        mycursor.execute(sql1,val2)
        mydb.commit()
        return render(request,'logoutp.html',{'status':'yes'})
    else:
        return render(request,'logoutp.html',{'status':'ENTER DETAILS'})


def doctor(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
        mycursor=mydb.cursor()
        sql="select name ,password from doctor where  name = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'doctor2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'doctor.html',{'result':'failure'})

    else:
        return render(request,'doctor.html',{'result':'registration page!!'})
def dct2(request):
    return render(request,'doctor2.html',{})

def prq(request):
    if request.method=='POST':
        up1=request.POST['pr1']
        up2=request.POST['pr2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
        mycursor=mydb.cursor()
        sql2='update sndapp set status=%s where  name=(%s) and dept = (%s)'
        val3=("approved",up1,up2,)
        mycursor.execute(sql2,val3)
        mydb.commit()
        return render(request,'prq.html',{'status1':"value updated"})
    else:
        return render(request,'prq.html',{'status1':'please enter the value!!!'})

def pinfo(request):
    if request.method=='POST':
        pc=request.POST['rec1']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
        mycursor=mydb.cursor()
        sql="select * from patient where name = %s "
        val=(pc,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'pinfo.html',{'result':data})
    else:
      return render(request,'pinfo.html',{'result':''})
def hreport(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
            reg7 = request.POST['r7']
            reg8 = request.POST['r8']
            reg9 = request.POST['r9']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 or len(reg7)==0 or len(reg8)==0 or len(reg9)==0 :
                return render(request,'hreport.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
                mycursor=mydb.cursor()
                sql="insert into hreport (name,dept,age,gender,height,weight,bp,sugar,report)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,reg7,reg8,reg9,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'hreport.html',{'result':'register succesfully!..'})
    else:
        return render(request,'hreport.html',{'result':'health report!..'})

def presc(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
         
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 :
                return render(request,'prescripd.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
                mycursor=mydb.cursor()
                sql="insert into priscription (name,dept,age,gender,date,prescrip)values(%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'prescripd.html',{'result':'register succesfully!..'})
    else:
         return render(request,'prescripd.html',{'result':'health report!..'})

def rqfdct(request):
    if request.method=='POST':
        pc=request.POST['rec1']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
        mycursor=mydb.cursor()
        sql="select * from sndapp where name = %s "
        val=(pc,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'rqfdc.html',{'result':data})
    else:
        return render(request,'rqfdc.html',{'result':''})

def prescriptp(request):
    if request.method=='POST':
        pc=request.POST['rec1']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
        mycursor=mydb.cursor()
        sql="select * from priscription where name = %s "
        val=(pc,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'prescriptionp.html',{'result':data})
    else:
      return render(request,'prescriptionp.html',{'result':''})


def cloudlet(request):
    if request.method == "POST":
        val1 = request.POST['a1']
        val2 = request.POST['a2']
        val1 = val1.lower() 
        val2 = val2.lower() 
        if val1=="admin" and val2=="admin":
            return render(request,'cloud2.html',{'result':'login successfully!..'})
        else:
            return render(request,'cloudlet.html',{'result':'failure'})
    else:
        return render(request,'cloudlet.html',{'result':'login page'})


def adddct(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
            reg7 = request.POST['r7']
            reg8 = request.POST['r8']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 or len(reg7)==0 or len(reg8)==0 :
                return render(request,'doctorreg.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
                mycursor=mydb.cursor()
                sql="insert into doctor (name,age,mobile,email,password,gender,dept,date)values(%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,reg7,reg8,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'doctorreg.html',{'result':'register succesfully!..'})
    else:
         return render(request,'doctorreg.html',{'result':'registration page'})
    

def dctinfo(request):
    
    if request.method=='POST':
        pc=request.POST['rec1']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
        mycursor=mydb.cursor()
        sql="select * from doctor where name = %s "
        val=(pc,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'doctorinfo.html',{'result':data})
    else:
      return render(request,'doctorinfo.html',{'result':''})

def pinfocloud(request):
    if request.method=='POST':
        pc=request.POST['rec1']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
        mycursor=mydb.cursor()
        sql="select * from patient where name = %s "
        val=(pc,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewpat.html',{'result':data})
    else:
      return render(request,'viewpat.html',{'result':''})

def intruder(request):
    if request.method=='POST':
        pc=request.POST['rec1']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
        mycursor=mydb.cursor()
        sql="select * from patient where name = %s "
        val=(pc,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'intruder.html',{'result':data})
    else:
      return render(request,'intruder.html',{'result':''})


def change(request):
    if request.method=='POST':
        up1=request.POST['pr1']
        up2=request.POST['pr2']
        id=int(request.POST['id'])
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
        mycursor=mydb.cursor()
        sql2='update patient set intruder=%s ,  name=(%s), dept=(%s) where patientid = %s'
        val3=("some one change yor data",up1,up2,id)
        mycursor.execute(sql2,val3)
        mydb.commit()
        return render(request,'change.html',{'status1':"value updated"})
    else:
        return render(request,'change.html',{'status1':'please enter the value!!!'})



def intrudc(request):
    if request.method=='POST':
        pc=request.POST['rec1']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="privacy")
        mycursor=mydb.cursor()
        sql="select * from patient where name = %s "
        val=(pc,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'intruderc.html',{'result':data})
    else:
      return render(request,'intruderc.html',{'result':''})
