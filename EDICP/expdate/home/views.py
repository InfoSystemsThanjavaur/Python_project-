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
            return render(request,'admin2.html',{'result':'login succesfully'})
        else:
            return render(request,'admin.html',{'result':'failure'})
    else:
        return render(request,'admin.html',{'result':'login page'})
   
def user(request):
    if request.method == "POST":
        val4 = request.POST['u1']
        val5 = request.POST['u2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
        mycursor=mydb.cursor()
        sql="select email ,password from register where  email = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)

        c=mycursor.fetchall()
        if c:
            return render(request,'USER2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'user.html',{'result':'failure'})

    else:
        return render(request,'user.html',{'result':'registration page!!'})
   
def register(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
            reg7 = request.POST['r7']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0 or len(reg7)==0 :
                return render(request,'reg.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
                mycursor=mydb.cursor()
                sql="insert into register (name,mobile,email,password,gender,dept,date)values(%s,%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,reg7,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'reg.html',{'result':'register succesfully!..'})
    else:
         return render(request,'reg.html',{'result':'registration page'})
    
def condt(request):
    if request.method=='POST':
        pc=request.POST['rec1']
        
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
        mycursor=mydb.cursor()
        sql="select * from register where name = %s "
        val=(pc,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'condt.html',{'result':data})
    else:
      return render(request,'condt.html',{'result':''})
               
def medicine(request):
    

        if request.method == "POST":
            po1 = request.POST['p1']
            po2 = request.POST['p2']
            po3 = request.POST['p3']
            po4 = request.POST['p4']
            po5 = request.POST['p5']
            po6 = request.POST['p6']
            
            if len(po1)== 0 or len(po2)==0 or len(po3)==0 or len(po4)==0 or len(po5)==0 or len(po6)==0 :
                return render(request,'medicine.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
                mycursor=mydb.cursor()
                sql="insert into medicine(medtype,medname,amount,quantity,manfacdt,expdt)values(%s,%s,%s,%s,%s,%s)"
                val=(po1,po2,po3,po4,po5,po6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'medicine.html',{'result':'medicine added'})
        else:
             return render(request,'medicine.html',{'result':'enter medicenes!..'})

def clrpro (request):
    if request.method=='POST':
        del1=request.POST['c1']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
        mycursor=mydb.cursor()
        sql1='delete from medicine where medtype =(%s)'
        val2=(del1,)
        mycursor.execute(sql1,val2)
        mydb.commit()
        return render(request,'clrprod.html',{'status':'yes'})
    else:
        return render(request,'clrprod.html',{'status':'ENTER MEDICINETYPE'})
    
    
def profile(request):
    if request.method=='POST':
        pc1=request.POST['rec1']
        pc2=request.POST['rec2']
        
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
        mycursor=mydb.cursor()
        sql="select * from register where consumerid = %s and where name = %s "
        val=(pc1,pc2,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'condt.html',{'result':data})
    else:
      return render(request,'condt.html',{'result':''})


            
def meddt(request):
    if request.method=='POST':
        pc1=request.POST['pro1']
        pc2=request.POST['pro2']
        
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
        mycursor=mydb.cursor()
        sql="select * from medicine where medtype = %s and  medname = %s "
        val=(pc1,pc2,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'meddt.html',{'result':data})
    else:
      return render(request,'meddt.html',{'result':''})


def logout(request):
    if request.method=='POST':
        del1=request.POST['c1']
        del2=request.POST['c2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
        mycursor=mydb.cursor()
        sql1='delete from register where name =(%s) and email =(%s)'
        val2=(del1,del2,)
        mycursor.execute(sql1,val2)
        mydb.commit()
        return render(request,'logout.html',{'status':'LOGOUT SUCCESFULLY!..'})
    else:
        return render(request,'logout.html',{'status':'ENTER DETAILS'})


def fedback(request):
    if request.method == "POST":
        val1 = request.POST['t1']
        val2 = request.POST['t2']
        val2 = request.POST['t3']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
        mycursor=mydb.cursor()
        sql="insert into feedback(name,feedbck)values(%s,%s)"
        val=(val1,val2)
        mycursor.execute(sql,val)
        mydb.commit()
        return render(request,'feedback.html',{'result':"thanks for your valuable feedback!.."})
    
    else:
        return render(request,'feedback.html',{})

def hospital(request):
    return render(request,'hospital.html',{})
def cntus(request):
    if request.method == "POST":
            po1 = request.POST['p1']
            po2 = request.POST['p2']
            po3 = request.POST['p3']
            po4 = request.POST['p4']
            po5 = request.POST['p5']
            po6 = request.POST['p6']
            po7 = request.POST['p7']
            po8 = request.POST['p8']
            if len(po1)== 0 or len(po2)==0 or len(po3)==0 or len(po4)==0 or len(po5)==0 or len(po6)==0 or len(po7)==0 or len(po8)==0:
                return render(request,'cntus.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
                mycursor=mydb.cursor()
                sql="insert into hospital(hosname,dept,medtype,medname,price,quantity,mandt,expdt)values(%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(po1,po2,po3,po4,po5,po6,po7,po8,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'cntus.html',{'result':'register successfully!..'})
    else:
         return render(request,'cntus.html',{'result':'registration page!..'})



def hlogout(request):
    if request.method=='POST':
        del1=request.POST['c1']
        del2=request.POST['c2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
        mycursor=mydb.cursor()
        sql1='delete from hospital where hosname =(%s) and dept =(%s)'
        val2=(del1,del2)
        mycursor.execute(sql1,val2)
        mydb.commit()
        return render(request,'hlogout.html',{'status':'yess'})
    else:
        return render(request,'hlogout.html',{'status':'ENTER DETAILS'})

   
def clrstck(request):
    if request.method=='POST':
        del2=request.POST['c1']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
        mycursor=mydb.cursor()
        sql2='update hospital set medtype=%s , medname=%s where hosname=%s'
        val3=("NULL","NULL",del2)
        mycursor.execute(sql2,val3)
        mydb.commit()
        return render(request,'clrstack.html',{'status1':"yess"})
    else:
        return render(request,'clrstack.html',{'status1':'please enter the stack!!!'})
    

           
def hviews(request):
    if request.method=='POST':
        pc1=request.POST['pro1']
        pc2=request.POST['pro2']
        
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
        mycursor=mydb.cursor()
        sql="select * from hospital where hosname = %s and  dept = %s "
        val=(pc1,pc2,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewdt.html',{'result':data})
    else:
      return render(request,'viewdt.html',{'result':''})

def aviews(request):
    if request.method=='POST':
        
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="expiry")
        mycursor=mydb.cursor()
        sql="select * from hospital"
        
        mycursor.execute(sql,)
        data=mycursor.fetchall()
        print(data)
        return render(request,'views.html',{'result':data})
    else:
      return render(request,'views.html',{'result':''})
