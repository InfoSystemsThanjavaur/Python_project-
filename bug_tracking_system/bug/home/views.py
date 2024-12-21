from django.shortcuts import render
import mysql.connector
def sample(request):
    return render(request,'index.html')

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


def reg(request):
     return render(request,'reg.html',{})

def ureg(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
        
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 :
                return render(request,'userreg.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
                mycursor=mydb.cursor()
                sql="insert into userreg (name,mobile,email,password,gender,date)values(%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'userreg.html',{'result':'register succesfully!..'})
    else:
         return render(request,'userreg.html',{'result':'registration page'})
  #  return render(request,'userreg.html',{})

def treg(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
            reg7 = request.POST['r7']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 or len(reg7)==0 :
                return render(request,'treg.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
                mycursor=mydb.cursor()
                sql="insert into testreg (name,mobile,email,jobrole,password,gender,date)values(%s,%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,reg7,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'treg.html',{'result':'register succesfully!..'})
    else:
         return render(request,'treg.html',{'result':'registration page'})
    # return render(request,'treg.html',{})
def dreg(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
            reg7 = request.POST['r7']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 or len(reg7)==0 :
                return render(request,'dreg.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
                mycursor=mydb.cursor()
                sql="insert into dreg (name,mobile,email,jobrole,password,gender,date)values(%s,%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,reg7,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'dreg.html',{'result':'register succesfully!..'})
    else:
         return render(request,'dreg.html',{'result':'registration page'})
    #return render(request,'dreg.html',{})

def user(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql="select name ,password from userreg where  name = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'user2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'user.html',{'result':'failure'})
    else:
        return render(request,'user.html',{'result':'loginpage!!'})

def tester(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql="select name ,password from testreg where  name = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'tester2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'tester.html',{'result':'failure'})
    else:
        return render(request,'tester.html',{'result':'loginpage!!'})

def developer(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql="select name ,password from dreg where  name = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'developer2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'developer.html',{'result':'failure'})
    else:
        return render(request,'developer.html',{'result':'loginpage!!'})


def viewdt(request):
     return render(request,'viewdt.html',{'result':''})

def udata(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql="select * from userreg "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'udata.html',{'result':data})
    else:
      return render(request,'udata.html',{'result':''})
     #return render(request,'udata.html',{})
def ddata(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql="select * from dreg "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'ddata.html',{'result':data})
    else:
      return render(request,'ddata.html',{'result':''})
    # return render(request,'ddata.html',{})
def tdata(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql="select * from dreg "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'tdata.html',{'result':data})
    else:
      return render(request,'tdata.html',{'result':''})
     #return render(request,'tdata.html',{})

def asignbug(request):
    if request.method == "POST":
        val1 = request.POST['r1']
        val2 = request.POST['r2']
        val3 = request.POST['r3']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql="insert into assbug(name,problem)values(%s,%s)"
        val=(val1,val2)
        mycursor.execute(sql,val)
        mydb.commit()
        return render(request,'assignbug.html',{'result':"sent successfully"})
    
    else:
        return render(request,'assignbug.html',{'result':'assignbug'})

def upro(request):
        if request.method=='POST':
            pc=request.POST['rec1']
        
            mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
            mycursor=mydb.cursor()
            sql="select * from userreg where userid = %s "
            val=(pc,)
            mycursor.execute(sql,val)
            data=mycursor.fetchall()
            return render(request,'uprofile.html',{'result':data})
        else:
            return render(request,'uprofile.html',{'result':''})

def addbug(request):
    if request.method == "POST":
        val1 = request.POST['r1']
        val2 = request.POST['r2']
        val3 = request.POST['r3']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql="insert into bugdt(name,bug,date)values(%s,%s,%s)"
        val=(val1,val2,val3,)
        mycursor.execute(sql,val)
        mydb.commit()
        return render(request,'addbug.html',{'result':"sent successfully"})
    
    else:
        return render(request,'addbug.html',{'result':'enter bug details!..'})

def viewasg(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql="select * from bugdt "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewbug.html',{'result':data})
    else:
      return render(request,'viewbug.html',{'result':''})


def asigndev(request):
    if request.method == "POST":
        val1 = request.POST['r1']
        val2 = request.POST['r2']
        val3 = request.POST['r3']
        val4 = request.POST['r4']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql="insert into asgdev(bugid,problem,devid,date)values(%s,%s,%s,%s)"
        val=(val1,val2,val3,val4,)
        mycursor.execute(sql,val)
        mydb.commit()
        return render(request,'asgdev.html',{'result':"sent successfully"})
    
    else:
        return render(request,'asgdev.html',{'result':'assign developer'})
    
def sndrpt(request):
    if request.method == "POST":
        val1 = request.POST['r1']
        val2 = request.POST['r2']
        val3 = request.POST['r3']
        val4 = request.POST['r4']
        val4 = request.POST['r4']
        val5 = request.POST['r5']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql="insert into report(bugid,solution,prodesc,soldesc,date)values(%s,%s,%s,%s,%s)"
        val=(val1,val2,val3,val4,val5,)
        mycursor.execute(sql,val)
        mydb.commit()
        return render(request,'sndrpt.html',{'result':"sent successfully"})
    
    else:
        return render(request,'sndrpt.html',{'result':'report!..'})

def viewasgbug(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql="select * from ASGDEV "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewasgbug.html',{'result':data})
    else:
      return render(request,'viewasgbug.html',{'result':''})

def viewslnad(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql="select * from report "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewslnad.html',{'result':data})
    else:
      return render(request,'viewslnad.html',{'result':''})

def VIEWSLNUS(request):
        if request.method=='POST':
            pc=request.POST['rec1']
        
            mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
            mycursor=mydb.cursor()
            sql="select * from report where bugid = %s "
            val=(pc,)
            mycursor.execute(sql,val)
            data=mycursor.fetchall()
            return render(request,'viewslnus.html',{'result':data})
        else:
            return render(request,'viewslnus.html',{'result':''})

def addsln(request):
    if request.method=='POST':
        r2=request.POST['r2']
        r3=request.POST['r3']
        r1=request.POST['r1']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="bug")
        mycursor=mydb.cursor()
        sql2='update report set solution=%s, soldesc=%s where bugid = %s'
        val3=(r2,r3,r1,)
        mycursor.execute(sql2,val3)
        mydb.commit()
        return render(request,'addsln.html',{'status1':"solution updated"})
    else:
        return render(request,'addsln.html',{'status1':'enter solution!!!'})
    #return render(request,'addsln.html',{})
