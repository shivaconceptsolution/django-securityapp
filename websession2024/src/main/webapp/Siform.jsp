<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
  <form action="SiServlet" method="post">
     <input type="text" placeholder="Enter P" name="txtp" />
     <br/><br/>
     <input type="text" placeholder="Enter R" name="txtr" />
     <br/><br/>
     <input type="text" placeholder="Enter T" name="txtt" />
     <br/><br/>
     <input type="submit" name="btnsubmit" value="CalculateSI" />
  </form>
  <%
  if(request.getParameter("q")!=null)
  {
	  out.println("Result is "+request.getParameter("q"));
  }
  
  %>
</body>
</html>