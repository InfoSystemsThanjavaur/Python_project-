from django.shortcuts import render
import mysql.connector
def index(request):
    return render(request,'index.html',{})
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
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="load")
                mycursor=mydb.cursor()
                sql="insert into user (name,mobile,email,password,gender,date)values(%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'reg.html',{'result':'register succesfully!..'})
    else:
         return render(request,'reg.html',{'result':'registration page'})

def clogin(request):
    if request.method == "POST":
        val1 = request.POST['t1']
        val2 = request.POST['t2']
        val1 = val1.lower() 
        val2 = val2.lower() 
        if val1=="admin" and val2=="admin":
            return render(request,'cloudserver.html',{'result':'login succesfully'})
        else:
            return render(request,'clogin.html',{'result':'failure'})
    else:
        return render(request,'clogin.html',{'result':'login page'})
    #return render(request,'clogin.html',{})

def user(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="load")
        mycursor=mydb.cursor()
        sql="select name ,password from user where  name = %s and password = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'user2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'user.html',{'result':'failure'})
    else:
        return render(request,'user.html',{'result':'loginpage!!'})

def profile(request):
    
        if request.method=='POST':
            pc=request.POST['rec1']
        
            mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="load")
            mycursor=mydb.cursor()
            sql="select * from user where userid = %s "
            val=(pc,)
            mycursor.execute(sql,val)
            data=mycursor.fetchall()
            return render(request,'profile.html',{'result':data})
        else:
            return render(request,'profile.html',{'result':''})
      
def req(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
        
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 :
                return render(request,'req.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="load")
                mycursor=mydb.cursor()
                sql="insert into req (enterid,content,request)values(%s,%s,%s)"
                val=(reg1,reg2,reg3)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'req.html',{'result':'request sent to cloud!..'})
    else:
         return render(request,'req.html',{'result':'cloud page!..'})
   # return render(request,'req.html',{})

def cmt(request):
    if request.method == "POST":
        val1 = request.POST['r1']
        val2 = request.POST['r2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="load")
        mycursor=mydb.cursor()
        sql="insert into cmt(name,comments)values(%s,%s)"
        val=(val1,val2)
        mycursor.execute(sql,val)
        mydb.commit()
        return render(request,'comment.html',{'result':"sent successfully"})
    
    else:
        return render(request,'comment.html',{})




def cloud(request):
    return render(request,'cloudserver.html',{})
def deluser(request):
    if request.method=='POST':
        del1=request.POST['c1']
        del2=request.POST['c2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="load")
        mycursor=mydb.cursor()
        sql1='delete from user where name =(%s) and password =(%s)'
        val2=(del1,del2,)
        mycursor.execute(sql1,val2)
        mydb.commit()
        return render(request,'deluser.html',{'status':'REMOVE SUCCESFULLY!..'})
    else:
        return render(request,'deluser.html',{'status':'ENTER DETAILS'})

def rply(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="load")
        mycursor=mydb.cursor()
        sql="select * from cmt "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'rply.html',{'result':data})
    else:
      return render(request,'rply.html',{'result':''})

def dynlogin(request):
    if request.method == "POST":
        val1 = request.POST['t1']
        val2 = request.POST['t2']
        val1 = val1.lower() 
        val2 = val2.lower() 
        if val1=="admin" and val2=="admin":
            return render(request,'dynsch.html',{'result':'login succesfully'})
        else:
            return render(request,'dynlogin.html',{'result':'failure'})
    else:
        return render(request,'dynlogin.html',{'result':'login page'})
   # return render(request,'dynsch.html',{})

def setsch(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
        
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 :
                return render(request,'setsch.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="load")
                mycursor=mydb.cursor()
                sql="insert into schedule (userid,name,sch)values(%s,%s,%s)"
                val=(reg1,reg2,reg3,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'setsch.html',{'result':'schedule succesfully!..'})
    else:
         return render(request,'setsch.html',{'result':'schedule page!..'})

def logout(request):
    return render(request,'index.html',{})

def viewsch(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="load")
        mycursor=mydb.cursor()
        sql="select * from schedule "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewsch.html',{'result':data})
    else:
      return render(request,'viewsch.html',{'result':''})


def viewreq(request):
    if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="load")
        mycursor=mydb.cursor()
        sql="select * from req "
        val=()
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewreq.html',{'result':data})
    else:
      return render(request,'viewreq.html',{'result':''})

def load(request):
    if request.method == "POST":
        val4 = request.POST['a1']
        val5 = request.POST['a2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="load")
        mycursor=mydb.cursor()
        sql="select name ,sch from schedule where  name = %s and sch = %s"
        val=(val4,val5)
        mycursor.execute(sql,val)
        c=mycursor.fetchall()
        if c:
            return render(request,'loadbalancer2.html',{'result':'LOGIN SUCCESFULLY'})
        else:
            return render(request,'loadbalancer.html',{'result':'failure'})
    else:
        return render(request,'loadbalancer.html',{'result':'loginpage!!'})

def upldt(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            
        
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 :
                return render(request,'upldt.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="load")
                mycursor=mydb.cursor()
                sql="insert into data (name,mobile,email,data,date)values(%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'upldt.html',{'result':'register succesfully!..'})
    else:
         return render(request,'upldt.html',{'result':'registration page'})

def viewdata(request):
    if request.method=='POST':
        pc=request.POST['rec1']
        
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="load")
        mycursor=mydb.cursor()
        sql="select * from data where userid = %s "
        val=(pc,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'viewdata.html',{'result':data})
    else:
      return render(request,'viewdata.html',{'result':''})
    #return render(request,'viewdata.html',{})