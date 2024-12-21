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

def ad2(request):
    return render(request,'ad2.html',{})


def addp(request):
    if request.method == "POST":
            po1 = request.POST['p1']
            po2 = request.POST['p2']
            po3 = request.POST['p3']
            po4 = request.POST['p4']
            po5 = request.POST['p5']
            po6 = request.POST['p6']
            if len(po1)== 0 or len(po2)==0 or len(po3)==0 or len(po4)==0 or len(po5)==0 or len(po6)==0 :
                return render(request,'addp.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
                mycursor=mydb.cursor()
                sql="insert into addfood(foodtype,foodname,price,quantity,manfactdt,expdt)values(%s,%s,%s,%s,%s,%s)"
                val=(po1,po2,po3,po4,po5,po6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'addp.html',{'result':'added successfully!..'})
    else:
         return render(request,'addp.html',{'result':'enter products!..'})

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
                return render(request,'reg.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
                mycursor=mydb.cursor()
                sql="insert into ureg (name,mobile,email,password,gender,date)values(%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'ureg.html',{'result':'register succesfully!..'})
    else:
         return render(request,'ureg.html',{'result':'registration page'})
  
def sreg(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
        
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 :
                return render(request,'sreg.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
                mycursor=mydb.cursor()
                sql="insert into sreg (name,mobile,email,password,gender,date)values(%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'sreg.html',{'result':'register succesfully!..'})
    else:
         return render(request,'sreg.html',{'result':'registration page'})


def viewu(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
        mycursor=mydb.cursor()
        sql="select * from ureg "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewu.html',{'result':data})
    else:
      return render(request,'viewu.html',{'result':''})




def views(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
        mycursor=mydb.cursor()
        sql="select * from sreg "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'views.html',{'result':data})
    else:
      return render(request,'views.html',{'result':''})

def user(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
        mycursor=mydb.cursor()
        sql="select name ,password from ureg where  name = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'user2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'user.html',{'result':'failure'})
    else:
        return render(request,'user.html',{'result':'loginpage!!'})


def seller(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
        mycursor=mydb.cursor()
        sql="select name ,password from sreg where  name = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'seller2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'seller.html',{'result':'failure'})
    else:
        return render(request,'seller.html',{'result':'loginpage!!'})
 
def selpro(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
        mycursor=mydb.cursor()
        sql="select * from sreg "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'selpro.html',{'result':data})
    else:
      return render(request,'selpro.html',{'result':''})


def addps(request):
    if request.method == "POST":
            po1 = request.POST['p1']
            po2 = request.POST['p2']
            po3 = request.POST['p3']
            po4 = request.POST['p4']
            po5 = request.POST['p5']
            po6 = request.POST['p6']
            if len(po1)== 0 or len(po2)==0 or len(po3)==0 or len(po4)==0 or len(po5)==0 or len(po6)==0 :
                return render(request,'addps.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
                mycursor=mydb.cursor()
                sql="insert into sellerfood(foodtype,foodname,price,quantity,manfacdt,expdt)values(%s,%s,%s,%s,%s,%s)"
                val=(po1,po2,po3,po4,po5,po6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'addps.html',{'result':'added successfully!..'})
    else:
         return render(request,'addps.html',{'result':'enter products!..'})


def viewsp(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
        mycursor=mydb.cursor()
        sql="select * from sellerfood "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewsp.html',{'result':data})
    else:
      return render(request,'viewsp.html',{'result':''})
    
def logout(request):
    if request.method=='POST':
        del1=request.POST['c1']
        del2=request.POST['c2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
        mycursor=mydb.cursor()
        sql1='delete from sreg where name =(%s) and password =(%s)'
        val2=(del1,del2,)
        mycursor.execute(sql1,val2)
        mydb.commit()
        return render(request,'logout.html',{'status':'LOGOUT SUCCESFULLY!..'})
    else:
        return render(request,'logout.html',{'status':'ENTER DETAILS'})
    

def logoutu(request):
    if request.method=='POST':
        del1=request.POST['c1']
        del2=request.POST['c2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
        mycursor=mydb.cursor()
        sql1='delete from ureg where name =(%s) and password =(%s)'
        val2=(del1,del2,)
        mycursor.execute(sql1,val2)
        mydb.commit()
        return render(request,'logoutu.html',{'status':'LOGOUT SUCCESFULLY!..'})
    else:
        return render(request,'logoutu.html',{'status':'ENTER DETAILS'})
    

def viewsselpro(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
        mycursor=mydb.cursor()
        sql="select * from sellerfood "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewsselpr.html',{'result':data})
    else:
      return render(request,'viewsselpr.html',{'result':''})
    
def viewsupro(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
        mycursor=mydb.cursor()
        sql="select * from addfood "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewsupro.html',{'result':data})
    else:
      return render(request,'viewsupro.html',{'result':''})
    
'''def order(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
            reg7 = request.POST['r7']
         
            print(reg1 , reg2,reg3,reg4, reg5, reg6,reg7)
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 or len(reg7)==0:
                return render(request,'ordpro.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
                mycursor=mydb.cursor()
                sql="insert into order(name,mobile,password,gender,date,address,order)values(%s,%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,reg7)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'ordrpro.html',{'result':'order succesfully!..'})
    else:
         return render(request,'ordpro.html',{'result':'ENTER YOUR ORDER!..'})'''



 
def order(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
            reg7 = request.POST['r7']

            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 or len(reg7)==0 :
                return render(request,'ordpro.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
                mycursor=mydb.cursor()
                sql="insert into orderp values(%s,%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,reg7,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'ordpro.html',{'result':'order succesfully!..'})
    else:
         return render(request,'ordpro.html',{'result':'enter order!..'})


def viewreq(request):
    if request.method=='POST':
        del2=request.POST['c1']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
        mycursor=mydb.cursor()
        sql2='update orderp set status=%s where name=%s'
        val3=("ORDER CONFIRMED",del2)
        mycursor.execute(sql2,val3)
        mydb.commit()
        return render(request,'viewreq.html',{'status1':"yess"})
    else:
        return render(request,'viewreq.html',{'status1':'update request'})

def viewordu(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
        mycursor=mydb.cursor()
        sql="select * from orderp "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'vieword.html',{'result':data})
    else:
      return render(request,'vieword.html',{'result':''})

def track(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="organic")
        mycursor=mydb.cursor()
        sql="select * from orderp "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'track.html',{'result':data})
    else:
      return render(request,'track.html',{'result':''})
    #return render(request,'track.html',{})