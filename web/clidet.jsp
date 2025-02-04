
<%@ page import="java.io.*;"%>	
<%@ page import="java.sql.*;"%>
<html><center>
<body>
<form action="clidet.jsp"method=post>
<table border=10 bgcolor="aquamarine" cellspacing=5 cellpadding=5>
<tr>
<th colspan=2>CLIENT DETAILS
</tr>
<tr>
<tr>
<th> UserName
<td><input type=text name=t1></tr>
<tr>
<th>User Password
<td><input type=text name=t2></tr>
<tr>
<th>Emil id
<td><input type=text name=t3></tr>
<tr>
<th>ServerAPI
<td><input type=text name=t4></tr>
<tr>
<th>Server Name
<td><input type=text name=t5></tr>
<tr>
<th>Server Usage
<td><input type=text name=t6></tr>
<tr>
<th colspan=2>
<input type=submit name=b1 value="ADD"></tr>
<%
try
{
String Username=request.getParameter("t1");
int Userpassword=Integer.parseInt(request.getParameter("t2"));
String Emailid=request.getParameter("t3");
String ServerAPI=request.getParameter("t4");
String Servername=request.getParameter("t5");
String Serverusage=request.getParameter("t6");
if(request.getParameter("b1")!=null)
{
Class.forName("com.mysql.jdbc.Driver");
Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/web","root","root");
PreparedStatement ps=con.prepareStatement("Insert into user_details values(?,?,?,?,?,?)");
ps.setString(1,Username);
ps.setInt(2,Userpassword);
ps.setString(3,Emailid);
ps.setString(4,ServerAPI);
ps.setString(5,Servername);
ps.setString(6,Serverusage);
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
</table>
</form>
</body>
</center>
</html>
