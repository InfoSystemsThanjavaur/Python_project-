
<%@ page import="java.io.*;"%>
<%@ page import="java.sql.*;"%>
<html><center>
<body>
<form action="cyberdet.jsp"method=post>
<table border=10 bgcolor="aquamarine" cellspacing=5 cellpadding=5>
<tr>
<th colspan=2>CYBER SECURITY REGISTER
</tr>
<tr>
<tr>
<th> SECURITY NAME:
<td><input type=text name=t1></tr>
<tr>
<th>SECURITY ID:
<td><input type=text name=t2></tr>
<tr>
<th>SECURITY SCAN ID:
<td><input type=text name=t3></tr>
<tr>
<th>SECURITY HACKING:
<td><input type=text name=t4></tr>
<tr>
<th>HACKING PROTOCOL:
<td><input type=text name=t5></tr>
<tr>
<th>HACKING SERVER:
<td><input type=text name=t6></tr>
<tr>
<th colspan=2>
<input type=submit name=b1 value="ADD"></tr>
<%
try
{
String Securityname=request.getParameter("t1");
int Securityid=Integer.parseInt(request.getParameter("t2"));
int Securityscanid=Integer.parseInt(request.getParameter("t3"));
String Securityhacking=request.getParameter("t4");
String Hackingprotocol=request.getParameter("t5");
String Hackingserver=request.getParameter("t6");
if(request.getParameter("b1")!=null)
{
Class.forName("com.mysql.jdbc.Driver");
Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/web","root","root");
PreparedStatement ps=con.prepareStatement("Insert into cyber_security_register values(?,?,?,?,?,?)");
ps.setString(1,Securityname);
ps.setInt(2,Securityid);
ps.setInt(3,Securityscanid);
ps.setString(4,Securityhacking);
ps.setString(5,Hackingprotocol);
ps.setString(6,Hackingserver);
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
