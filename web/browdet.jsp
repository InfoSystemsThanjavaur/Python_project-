
<%@ page import="java.io.*;"%>
<%@ page import="java.sql.*;"%>
<html><center>
<body>
<form action="browdet.jsp" method=post>
<table border=10 bgcolor="bisque" cellspacing=5 cellpadding=5>
<tr>
<th colspan=2>BROWSER DETAILS
</tr>
<tr>
<tr>
<th>Browser Name
<td><input type=text name=t1></tr>
<tr>
<th>Browser Speed
<td><input type=text name=t2></tr>
<tr>
<th>Scan id
<td><input type=text name=t3></tr>
<tr>
<th>Browser Authority 
<td><input type=text name=t4></tr>
<tr>
<th colspan=2>
<input type=submit name=b1 value="ADD"></tr>
<%
try
{
String browsername=request.getParameter("t1");
int browserspeed=Integer.parseInt(request.getParameter("t2"));
String scanid=request.getParameter("t3");
String browserauthor=request.getParameter("t4");
if(request.getParameter("b1")!=null)
{
Class.forName("com.mysql.jdbc.Driver");
Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/web","root","root");
PreparedStatement ps=con.prepareStatement("Insert into browser_details values(?,?,?,?)");
ps.setString(1,browsername);
ps.setInt(2,browserspeed);
ps.setString(3,scanid);
ps.setString(4,browserauthor);
int x=ps.executeUpdate();
if(x>0)
{
out.println("<script>alert('Insert success');</script>");
}
else
{
out.println("<script>alert('Insert failed');</script>");
}}}
catch(Exception e)
{
out.println(e);
}
%>
</table>
<a href="brodetscan.html">click</a></form></body></html>
