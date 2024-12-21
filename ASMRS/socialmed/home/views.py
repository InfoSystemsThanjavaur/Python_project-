from django.shortcuts import render
import mysql.connector
def sample(request):
 
    return render(request,'index.html',{})
def sample1(request):
    if request.method == "POST":
        val1 = request.POST['t1']
        val2 = request.POST['t2']
        val1 = val1.lower() 
        val2 = val2.lower() 
        if val1=="admin" and val2=="admin":
            return render(request,'admin2.html',{'result':'login succesfully'})
        else:
            return render(request,'admin.html',{'result':'failure'})
    else:
        return render(request,'admin.html',{'result':'login page'})

def sample2(request):
    if request.method == "POST":
            reg1 = request.POST['r1']
            reg2 = request.POST['r2']
            reg3 = request.POST['r3']
            reg4 = request.POST['r4']
            reg5 = request.POST['r5']
            reg6 = request.POST['r6']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 or len(reg6)==0:
                return render(request,'reg.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="socmedia")
                mycursor=mydb.cursor()
                sql="insert into register (name,mobile,email,password,gender,date)values(%s,%s,%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,reg5,reg6,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'reg.html',{'result':'register succesfully!..'})
    else:
         return render(request,'reg.html',{'result':'registration page'})
        
def sample3(request):
    if request.method == "POST":
        val4 = request.POST['u1']
        val5 = request.POST['u2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="socmedia")
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
def addctc(request):
   if request.method == "POST":
            reg1 = request.POST['a1']
            reg2 = request.POST['a2']
            reg3 = request.POST['a3']
            reg4 = request.POST['a4']
            if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg3)==0 or len(reg4)==0 :
                return render(request,'addctg.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="socmedia")
                mycursor=mydb.cursor()
                sql="insert into addctg(posttitle,postcategory,postdescription,date)values(%s,%s,%s,%s)"
                val=(reg1,reg2,reg3,reg4,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'addctg.html',{'result':'CATEGORY ADDED'})
   else:
       return render(request,'addctg.html',{'result':'ADD CATEGORY!..'})
def clrctg(request):
    if request.method=='POST':
        del1=request.POST['c1']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="socmedia")
        mycursor=mydb.cursor()
        sql1='delete from addctg where postid =(%s)'
        val2=(del1,)
        mycursor.execute(sql1,val2)
        mydb.commit()
        return render(request,'clrctg.html',{'status':'VALUE DELETED'})
    else:
        return render(request,'clrctg.html',{'status':'ENTER THE ID'})
def uplctg(request):
    if request.method == "POST":
        reg1 = request.POST['up1']
        reg2 = request.POST['up2']
        reg3 = request.POST['up3']
        reg4 = request.POST['up4']
        reg5 = request.POST['up5']
       
        if len(reg1)== 0 or len(reg2)==0 or len(reg3)==0 or len(reg3)==0 or len(reg4)==0 or len(reg5)==0 :
            return render(request,'uplctg.html',{'result':'Fill All'})
        else:
            mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="socmedia")
            mycursor=mydb.cursor()
            sql="insert into (arttitle,category,description,artsub,upload)values(%s,%s,%s,%s)"
            val=(reg1,reg2,reg3,reg4,reg5,)
            mycursor.execute(sql,val)
            mydb.commit()
        
            return render(request,'uplctg.html',{'result':'upload succesfully!..'})
      
    else:
        return render(request,'uplctg.html',{'result':'upload category!..'})
def recom(request):
    if request.method=='POST':
        pc=request.POST['rec1']
        
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="socmedia")
        mycursor=mydb.cursor()
        sql="select * from addctg where postcategory= %s "
        val=(pc,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        return render(request,'recomend.html',{'result':data})
    else:
      return render(request,'recomend.html',{'result':''})
    

def news(request):

        if request.method == "POST":
            new1 = request.POST['n1']
            new2 = request.POST['n2']
            new3 = request.POST['n3']
     
            if len(new1)== 0 or len(new2)==0 or len(new3)==0 :
                return render(request,'news.html',{'result':'Fill All!'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="socmedia")
                mycursor=mydb.cursor()
                sql="insert into newsfeed(newstitle,titlesub,newsctn)values(%s,%s,%s)"
                val=(new1,new2,new3,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'news.html',{'result':'CATEGORY ADDED'})
        else:
             return render(request,'news.html',{'result':'news feeds!..'})  
def post(request):
   
        if request.method == "POST":
            po1 = request.POST['p1']
            po2 = request.POST['p2']
            po3 = request.POST['p3']
            po4 = request.POST['p4']
            if len(po1)== 0 or len(po2)==0 or len(po3)==0 or len(po4)==0 :
                return render(request,'postadd.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="socmedia")
                mycursor=mydb.cursor()
                sql="insert into postadd(posttitle,postcategory,description,date)values(%s,%s,%s,%s)"
                val=(po1,po2,po3,po4,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'postadd.html',{'result':'CATEGORY ADDED'})
        else:
             return render(request,'postadd.html',{'result':'ADD YOUR POST'})
  
def com(request):
    if request.method=='POST':
            cmt=request.POST['cmt1']
            mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="socmedia")
            mycursor=mydb.cursor()
            sql="select * from postadd where postid= %s "
            val=(cmt,)
            mycursor.execute(sql,val)
            data=mycursor.fetchall()
            return render(request,'comment.html',{'result':data})
    else:
        return render(request,'comment.html',{'result':''})
        
    
    

def cmt1(request):
    if request.method=='POST':
        cmt1=request.POST['cs1']
        cmt2=request.POST['cs2']
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="socmedia")
        mycursor=mydb.cursor()
        sql2='update postadd set comment=%s where postid=%s'
        
        val3=(cmt2,cmt1,)
        mycursor.execute(sql2,val3)
        mydb.commit()
        return render(request,'cmtsec.html',{'status1':"comment added"})
    else:
        return render(request,'cmtsec.html',{'status1':'enter your comments!..'})


def view(request):
    if request.method=='POST':
            cmt=request.POST['cmt1']
            mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="socmedia")
            mycursor=mydb.cursor()
            sql="select * from postadd where postid= %s "
            val=(cmt,)
            mycursor.execute(sql,val)
            data=mycursor.fetchall()
            return render(request,'viewact.html',{'result':data})
    else:
        return render(request,'viewact.html',{'result':''})