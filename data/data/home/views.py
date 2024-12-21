from django.shortcuts import render
import mysql.connector
def sample(request):
    return render(request,'index.html',{})

def down(request):
    if request.method == "POST":
        val1 = request.POST['t1']
        val2 = request.POST['t2']
        val1 = val1.lower() 
        val2 = val2.lower() 
        if val1=="dataowner" and val2=="dataowner":
            return render(request,'do2.html',{'result':'login succesfully'})
        else:
            return render(request,'dataown.html',{'result':'failure'})
    else:
        return render(request,'dataown.html',{'result':'login page'})

def downm(request):
    if request.method == "POST":
            po1 = request.POST['p1']
            po2 = request.POST['p2']
            po3 = request.POST['p3']
            po4 = request.POST['p4']
            po5 = request.POST['p5']
            if len(po1)== 0 or len(po2)==0 or len(po3)==0 or len(po4)==0 or len(po5)==0 :
                return render(request,'downm.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="data")
                mycursor=mydb.cursor()
                sql="insert into dataowner(gid,imgname,authch,imagetype,imgctype)values(%s,%s,%s,%s,%s)"
                val=(po1,po2,po3,po4,po5,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'downm.html',{'result':'add successfully!..'})
    else:
         return render(request,'downm.html',{'result':'data owner!..'})
   # return render(request,'downm.html',{})


def keygen(request):
    if request.method == "POST":
        val1 = request.POST['a1']
        val2 = request.POST['a2']
        val1 = val1.lower() 
        val2 = val2.lower() 
        if val1=="key" and val2=="key":
            return render(request,'k2.html',{'result':'login succesfully'})
        else:
            return render(request,'keygen.html',{'result':'failure'})
    else:
        return render(request,'keygen.html',{'result':'login page'})

def keym(request):
    if request.method == "POST":
            po1 = request.POST['p1']
            po2 = request.POST['p2']
            po3 = request.POST['p3']
            po4 = request.POST['p4']
            po5 = request.POST['p5']
            po6 = request.POST['p6']
         
            if len(po1)== 0 or len(po2)==0 or len(po3)==0 or len(po4)==0 or len(po5)==0 or len(po5)==0:
                return render(request,'keym.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="data")
                mycursor=mydb.cursor()
                sql="insert into key(uname,password,repass,fname,email,phno)values(%s,%s,%s,%s,%s,%s)"
                val=(po1,po2,po3,po4,po5,po6)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'keym.html',{'result':'add successfully!..'})
    else:
         return render(request,'keym.html',{'result':'data owner!..'})
 #  return render(request,'keym.html',{})

def auditting(request):
    return render(request,'auditting.html',{})
def audit(request):
    if request.method == "POST":
            po1 = request.POST['a1']
            po2 = request.POST['a2']
            po3 = request.POST['a3']
            po4 = request.POST['a4']
         
            if len(po1)== 0 or len(po2)==0 or len(po3)==0 or len(po4)==0 :
                return render(request,'audm.html',{'result':'Fill All'})
            else:
                mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="data")
                mycursor=mydb.cursor()
                sql="insert into aud(startid,name,contact,phno)values(%s,%s,%s,%s)"
                val=(po1,po2,po3,po4,)
                mycursor.execute(sql,val)
                mydb.commit()
                return render(request,'audm.html',{'result':'add successfully!..'})
    else:
         return render(request,'audm.html',{'result':'data owner!..'})
def cloud(request):
    if request.method == "POST":
        val1 = request.POST['t1']
        val2 = request.POST['t2']
        val1 = val1.lower() 
        val2 = val2.lower() 
        if val1=="cloud" and val2=="cloud":
            return render(request,'c2.html',{'result':'login succesfully'})
        else:
            return render(request,'cloud.html',{'result':'failure'})
    else:
        return render(request,'cloud.html',{'result':'login page'})

def climg(request):
    return render(request,'cloudimage.html',{})

def clser(request):
    return render(request,'cserver.html',{})