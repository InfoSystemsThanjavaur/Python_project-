<%@ include file="main.html"%>
<%@ page import="java.io.*;"%>
<html><center>
<body>
<form action="serverlog.jsp"method="post">
<table border=5 bgcolor="violet"cellspacing=10 cellpadding=10>
<tr>
<th colspan=2>SERVER LOGIN FORM
</tr>
<tr>
<th> UserName
<td><input type="text"name=t1>
</tr>
<th>Password
<td><input type="text"name=t2>
</tr>
<tr>
<th colspan=2><input type= "submit" name=b1 value="click">
</tr>
<%
try
{
String un=request.getParameter("t1");
String pw=request.getParameter("t2");
if(request.getParameter("b1") !=null)
{
if(un.equalsIgnoreCase("server")&&pw.equalsIgnoreCase("server"))
{response.sendRedirect("serdet.jsp");}
else
{
%>
<script>
alert("Login failed");
</script>
<%
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
