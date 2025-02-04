
<%@ page import="java.io.*;"%>
<%@ page import="java.sql.*;"%>
<html><center>
<body>
<form action="serdet.jsp"method=post>
<table border=10 bgcolor="aqua" cellspacing=5 cellpadding=5>
<tr>
<th colspan=2>SERVER DETAILS
</tr>
<tr>
<tr>
<th> Server Name
<td><input type=text name=t1></tr>
<tr>
<th>Server id
<td><input type=text name=t2></tr>
<tr>
<th>Server API
<td><input type=text name=t3></tr>
<tr>
<th>Server Password
<td><input type=text name=t4></tr>
<tr>
<th>Security Password
<td><input type=text name=t5></tr>
<tr>
<th>Security Authority
<td><input type=text name=t6></tr>
<tr>
<th colspan=2>
<input type=submit name=b1 value="ADD"></tr>
<%
try
{
String Servername=request.getParameter("t1");
int Serverid=Integer.parseInt(request.getParameter("t2"));
String ServerAPI=request.getParameter("t3");
int Serverpassword=Integer.parseInt(request.getParameter("t4"));
int Securitypassword=Integer.parseInt(request.getParameter("t5"));
String Securityauthority=request.getParameter("t6");
if(request.getParameter("b1")!=null)
{
Class.forName("com.mysql.jdbc.Driver");
Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/web","root","root");
PreparedStatement ps=con.prepareStatement("Insert into server_details values(?,?,?,?,?,?)");
ps.setString(1,Servername);
ps.setInt(2,Serverid);
ps.setString(3,ServerAPI);
ps.setInt(4,Serverpassword);
ps.setInt(5,Securitypassword);
ps.setString(6,Securityauthority);
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
