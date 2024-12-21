from django.shortcuts import render
import mysql.connector
def sample(request):
    return render(request,'index.html',{})


def admin(request):
    if request.method == "POST":
        val1 = request.POST['a1']
        val2 = request.POST['a2']
        val1 = val1.lower() 
        val2 = val2.lower() 
        if val1=="admin" and val2=="admin":
            return render(request,'ad2.html',{'result':'login successfully!..'})
        else:
            return render(request,'admin.html',{'result':'failure'})
    else:
        return render(request,'admin.html',{'result':'login page'})

def lrnadm(request):
    if request.method == "POST":
            po1 = request.POST['p1']
            po2 = request.POST['p2']
            po3 = request.POST['p3']
            po4 = request.POST['p4']
            po5 = request.POST['p5']
            po6 = request.POST['p6']
          
          
            if len(po1)== 0 or len(po2)==0 or len(po3)==0 or len(po4)==0 or len(po5)==0 or len(po6)==0:
                return render(request,'lrnadm.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="elearning")
                mycursor=mydb.cursor()
                sql="insert into adlearner(name,age,gender,password,native,date)values(%s,%s,%s,%s,%s,%s)"
                val=(po1,po2,po3,po4,po5,po6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'lrnadm.html',{'result':'admited successfully!..'})
    else:
         return render(request,'lrnadm.html',{'result':'add learner!..'})
def pmet(request):
    if request.method == "POST":
        val1 = request.POST['S1']
        val2 = request.POST['S2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="elearning")
        mycursor=mydb.cursor()
        sql="insert into material(studymat,notes)values(%s,%s)"
        val=(val1,val2)
        mycursor.execute(sql,val)
        mydb.commit()
        return render(request,'pmet.html',{'result':"yes"})
    else:
        return render(request,'pmet.html',{'result':'upload your notes!.'})

def lrn(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="elearning")
        mycursor=mydb.cursor()
        sql="select name ,password from adlearner where  name = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'learn2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'learn.html',{'result':'failure'})
    else:
        return render(request,'learn.html',{'result':'loginpage!!'})

def learn(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="elearning")
        mycursor=mydb.cursor()
        sql="select * from adlearner "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'lrn.html',{'result':data})
    else:
      return render(request,'lrn.html',{'result':''})

def ask(request):
    if request.method == "POST":
        val1 = request.POST['S1']
        val2 = request.POST['S2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="elearning")
        mycursor=mydb.cursor()
        sql="insert into question(name,query)values(%s,%s)"
        val=(val1,val2)
        mycursor.execute(sql,val)
        mydb.commit()
        return render(request,'ask.html',{'result':"yes"})
    else:
        return render(request,'ask.html',{'result':'enter query!.'})

def addfac(request):
    if request.method == "POST":
            po1 = request.POST['p1']
            po2 = request.POST['p2']
            po3 = request.POST['p3']
            po4 = request.POST['p4']
            po5 = request.POST['p5']
            po6 = request.POST['p6']
            po7 = request.POST['p7']
          
          
            if len(po1)== 0 or len(po2)==0 or len(po3)==0 or len(po4)==0 or len(po5)==0 or len(po6)==0 or len(po7):
                return render(request,'lrnadm.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="elearning")
                mycursor=mydb.cursor()
                sql="insert into faculty(name,age,gender,password,native,date,qualification)values(%s,%s,%s,%s,%s,%s)"
                val=(po1,po2,po3,po4,po5,po6,po7,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'addfac.html',{'result':'admited successfully!..'})
    else:
         return render(request,'addfac.html',{'result':'add learner!..'})

def faculty(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="elearning")
        mycursor=mydb.cursor()
        sql="select name ,password from faculty where  name = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'faculty2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'faculty.html',{'result':'failure'})
    else:
        return render(request,'faculty.html',{'result':'loginpage!!'})

def viewq(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="elearning")
        mycursor=mydb.cursor()
        sql="select * from question "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewq.html',{'result':data})
    else:
      return render(request,'viewq.html',{'result':''})

def resans(request):
    if request.method == "POST":
        val1 = request.POST['S1']
        val2 = request.POST['S2']
        val3 = request.POST['S3']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="elearning")
        mycursor=mydb.cursor()
        sql="insert into answer(name,question,answer)values(%s,%s,%s)"
        val=(val1,val2,val3,)
        mycursor.execute(sql,val)
        mydb.commit()
        return render(request,'resans.html',{'result':"yes"})
    else:
        return render(request,'resans.html',{'result':'enter your answer!..'})

def logout(request):
    if request.method=='POST':
        del1=request.POST['c1']
        del2=request.POST['c2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="elearning")
        mycursor=mydb.cursor()
        sql1='delete from faculty where name =(%s) and password =(%s)'
        val2=(del1,del2,)
        mycursor.execute(sql1,val2)
        mydb.commit()
        return render(request,'logout.html',{'status':'LOGOUT SUCCESFULLY!..'})
    else:
        return render(request,'logout.html',{'status':'ENTER DETAILS'})
def recsln(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="elearning")
        mycursor=mydb.cursor()
        sql="select * from answer "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'recsln.html',{'result':data})
    else:
      return render(request,'recsln.html',{'result':''})
   # return render(request,'recsln.html',{})