from django.shortcuts import render
import mysql.connector
def sample(request):
    return render(request,'index.html',{})


def user(request):
    return render(request,'user.html',{})

def reg(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
        
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 :
                return render(request,'reg.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
                mycursor=mydb.cursor()
                sql="insert into reg (name,mobile,email,password,gender,date)values(%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'register.html',{'result':'register succesfully!..'})
    else:
         return render(request,'register.html',{'result':'registration page'})
    
def user(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
        mycursor=mydb.cursor()
        sql="select name ,password from reg where  name = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'user2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'user.html',{'result':'failure'})
    else:
        return render(request,'user.html',{'result':'loginpage!!'})

def server(request):
    if request.method == "POST":
        val1 = request.POST['a1']
        val2 = request.POST['a2']
        val1 = val1.lower() 
        val2 = val2.lower() 
        if val1=="admin" and val2=="admin":
            return render(request,'s2.html',{'result':'login successfully!..'})
        else:
            return render(request,'server.html',{'result':'failure'})
    else:
        return render(request,'server.html',{'result':'login page'})

def viewsat(request):
   
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
        
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0:
                return render(request,'views.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
                mycursor=mydb.cursor()
                sql="insert into satellite (satname,satmodel,quantity,quality,price,proDdesc)values(%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'views.html',{'result':'register succesfully!..'})
    else:
         return render(request,'views.html',{'result':'registration page'})
   # return render(request,'views.html',{})

def purchased(request):
   
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
          
        
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 :
                return render(request,'purchased.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
                mycursor=mydb.cursor()
                sql="insert into purchased (satname,satmodel,quantity,address,phno)values(%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'purchased.html',{'result':'register succesfully!..'})
    else:
         return render(request,'purchased.html',{'result':'PURCHASE PAGE'})

def upldel(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
          
        
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0:
                return render(request,'upldel.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
                mycursor=mydb.cursor()
                sql="insert into upddel (satname,satmodel,toadd,deltime,deldate)values(%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'upldel.html',{'result':'update succesfully!..'})
    else:
         return render(request,'upldel.html',{'result':'update delevary '})
    # return render(request,'upldel.html',{})
def feedback(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
        
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 :
                return render(request,'feedback.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
                mycursor=mydb.cursor()
                sql="insert into feedback(satname,satmodel,review)values(%s,%s,%s)"
                val=(reg1,reg2,reg3,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'feedback.html',{'result':'sent succesfully!..'})
    else:
         return render(request,'feedback.html',{'result':'enter feedback '})
def analyser(request):
     return render(request,'analyser.html',{})

def cntserver(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg3)==0:
                return render(request,'cntser.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
                mycursor=mydb.cursor()
                sql="insert into cntser(sername,serpas,text,retypepas)values(%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'cntser.html',{'result':'sent succesfully!..'})
    else:
         return render(request,'cntser.html',{'result':'enter feedback '})

def behaviour(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg3)==0:
                return render(request,'behvior.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
                mycursor=mydb.cursor()
                sql="insert into behave(cname,cid,psat,feedback)values(%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'behvior.html',{'result':'sent succesfully!..'})
    else:
         return render(request,'behvior.html',{'result':'enter feedback '})

def products(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0:
                return render(request,'products.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
                mycursor=mydb.cursor()
                sql="insert into products(sname,smodel,purpose,sensor,speed,processor)values(%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'products.html',{'result':'sent succesfully!..'})
    else:
         return render(request,'products.html',{'result':'enter product '})


def report(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
           
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 :
                return render(request,'report.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
                mycursor=mydb.cursor()
                sql="insert into report(satname,satmodel,cond)values(%s,%s,%s)"
                val=(reg1,reg2,reg3,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'report.html',{'result':'sent succesfully!..'})
    else:
         return render(request,'report.html',{'result':'enter feedback '})

def vpurchased(request):
        if request.method=='POST':
            vp=request.POST['rec1']
            vp1 =request.POST['rec2']
            mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
            mycursor=mydb.cursor()
            sql="select * from purchased where satname = %s  and satmodel = %s "
            val=(vp,vp1,)
            mycursor.execute(sql,val)
            data=mycursor.fetchall()
            return render(request,'vpurchased.html',{'result':data})
        else:
            return render(request,'vpurchased.html',{'result':''})

def customer(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 :
                return render(request,'customer.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
                mycursor=mydb.cursor()
                sql="insert into customer(cname,cid,cloc,phno,email,ap)values(%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'customer.html',{'result':'sent succesfully!..'})
    else:
         return render(request,'customer.html',{'result':'enter product '})

def ordsat(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
        mycursor=mydb.cursor()
        sql="select * from purchased "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'ordsat.html',{'result':data})
    else:
      return render(request,'ordsat.html',{'result':''})

def addproducts(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
        mycursor=mydb.cursor()
        sql="select * from products "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'addpro.html',{'result':data})
    else:
      return render(request,'addpro.html',{'result':''})
def checkb(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
        mycursor=mydb.cursor()
        sql="select * from behave"
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'checkb.html',{'result':data})
    else:
      return render(request,'addpro.html',{'result':''})


def dailys(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="satellite")
        mycursor=mydb.cursor()
        sql="select * from satellite"
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'dailysales.html',{'result':data})
    else:
      return render(request,'dailysales.html',{'result':''})