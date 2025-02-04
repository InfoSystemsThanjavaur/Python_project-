
<%@ page import="java.io.*;"%>
<%@ page import="java.sql.*;"%>
<html><center>
<body>
<form action="addet.jsp"method=post>
<table border=10 bgcolor="aquamarine" cellspacing=5 cellpadding=5>
<tr>
<th colspan=2>ADMIN DETAILS
</tr>
<tr>
<tr>
<th> Name
<td><input type=text name=t1></tr>
<tr>
<th>Password
<td><input type=text name=t2></tr>
<tr>
<th>Retypepassword
<td><input type=text name=t3></tr>
<tr>
<th>Emailid
<td><input type=text name=t4></tr>
<tr>
<th>Address
<td><input type=text name=t5></tr>
<tr>
<th colspan=2>
<input type=submit name=b1 value="ADD"></tr>
<%
try
{
String Name=request.getParameter("t1");
int Password=Integer.parseInt(request.getParameter("t2"));
int Retypepassword=Integer.parseInt(request.getParameter("t3"));
String Emailid=request.getParameter("t4");
String Address=request.getParameter("t5");
if(request.getParameter("b1")!=null)
{
    Class.forName("com.mysql.jdbc.Driver");
    Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/web","root","root");
    PreparedStatement ps=con.prepareStatement("insert into admin_details values(?,?,?,?,?)");
    ps.setString(1,Name);
    ps.setInt(2,Password);
    ps.setInt(3,Retypepassword);
    ps.setString(4,Emailid);
    ps.setString(5,Address);
    int x=ps.executeUpdate();
if(x>0)
{
out.println("<script>alert('Insert success');</script>");
}
else
{
out.println("<script>alert('Insert failed');</script>");
}
}
}
catch(Exception e)
{
out.println(e);
}
%>
</table></form></body></center></html>
