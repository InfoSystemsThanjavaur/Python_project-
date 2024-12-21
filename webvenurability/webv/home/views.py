from django.shortcuts import render
import mysql.connector
def sample(request):
    return render(request,'index.html',{})

def register(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
            reg7 = request.POST['r7']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 or len(reg7)==0:
                return render(request,'reg.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
                mycursor=mydb.cursor()
                sql="insert into register(name,mobile,email,qualification,password,gender,date)values(%s,%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,reg7,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'reg.html',{'result':'register succesfully!..'})
    else:
         return render(request,'reg.html',{'result':'registration page'})
 


def std(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
        mycursor=mydb.cursor()
        sql="select name ,password from register where  name = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'stu2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'user.html',{'result':'failure'})
    else:
        return render(request,'user.html',{'result':'loginpage!!'})

  
  


def man(request):
    if request.method == "POST":
        val1 = request.POST['a1']
        val2 = request.POST['a2']
        val1 = val1.lower() 
        val2 = val2.lower() 
        if val1=="admin" and val2=="admin":
            return render(request,'man2.html',{'result':'login successfully!..'})
        else:
            return render(request,'management.html',{'result':'failure'})
    else:
        return render(request,'management.html',{'result':'login page'})

def addc(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
          
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 :
                return render(request,'addc.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
                mycursor=mydb.cursor()
                sql="insert into company(cmpname,cmptype,jobrole,address,password,date)values(%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'addc.html',{'result':'register succesfully!..'})
    else:
         return render(request,'addc.html',{'result':'add company!..'})
 

def sndapp(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']

          
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 :
                return render(request,'addc.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
                mycursor=mydb.cursor()
                sql="insert into application(name,mobile,email,date,appli)values(%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'sndapp.html',{'result':'register succesfully!..'})
    else:
         return render(request,'sndapp.html',{'result':'add company!..'})
   # return render(request,'sndapp.html',{})
def delcmpy(request):
    if request.method=='POST':
        del1=request.POST['c1']
        del2=request.POST['c2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
        mycursor=mydb.cursor()
        sql1='delete from company where cmpname =(%s) and password =(%s)'
        val2=(del1,del2,)
        mycursor.execute(sql1,val2)
        mydb.commit()
        return render(request,'delcmpy.html',{'status':'LOGOUT SUCCESFULLY!..'})
    else:
        return render(request,'delcmpy.html',{'status':'ENTER DETAILS'})

def viewcmpy(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
        mycursor=mydb.cursor()
        sql="select * from company "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewcmp.html',{'result':data})
    else:
      return render(request,'viewcmp.html',{'result':''})

def viewapp(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
        mycursor=mydb.cursor()
        sql="select * from application "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewapp.html',{'result':data})
    else:
      return render(request,'viewapp.html',{'result':''})
 
def cmpy(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
        mycursor=mydb.cursor()
        sql="select cmpname ,password from company where  cmpname = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'c2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'company.html',{'result':'failure'})
    else:
        return render(request,'company.html',{'result':'loginpage!!'})


def place(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0  :
                return render(request,'placement.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
                mycursor=mydb.cursor()
                sql="insert into placement(cname,ctype,jobrole,materials)values(%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'placement.html',{'result':'sent succesfully!..'})
    else:
         return render(request,'placement.html',{'result':'put placement!..'})

def sndrep(request):
    
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
    
            if len(reg1)== 0 or len(reg2)==0  :
                return render(request,'sndrep.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
                mycursor=mydb.cursor()
                sql="insert into genrep(stname,report)values(%s,%s)"
                val=(reg1,reg2,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'sndrep.html',{'result':'generate succesfully!..'})
    else:
         return render(request,'sndrep.html',{'result':'generate rep!..'})
 
def viewstu(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
        mycursor=mydb.cursor()
        sql="select * from register "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewstu.html',{'result':data})
    else:
      return render(request,'viewstu.html',{'result':''})

def viewgen(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
        mycursor=mydb.cursor()
        sql="select * from  genrep"
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewgen.html',{'result':data})
    else:
      return render(request,'viewgen.html',{'result':''})

def viewplace(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
        mycursor=mydb.cursor()
        sql="select * from placement "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewplace.html',{'result':data})
    else:
      return render(request,'viewplace.html',{'result':''})


def test(request):
    if request.method == "POST":
        val4 = request.POST['rec1']
   
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="web")
        mycursor=mydb.cursor()
        sql="select *  from genrep where  studentid = %s "
        val=(val4,)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'test.html',{'result':c})
        else:
            return render(request,'index.html',{'result':'yess'})
    else:
        return render(request,'test.html',{'result':''})
   # return render(request,'test.html',{})