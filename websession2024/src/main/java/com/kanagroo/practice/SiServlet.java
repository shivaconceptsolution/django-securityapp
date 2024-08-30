package com.kanagroo.practice;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class SiServlet
 */
@WebServlet("/SiServlet")
public class SiServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		float p = Float.parseFloat(request.getParameter("txtp"));
		float r = Float.parseFloat(request.getParameter("txtr"));
		float t = Float.parseFloat(request.getParameter("txtt"));
		float si = (p*r*t)/100;
		response.sendRedirect("Siform.jsp?q="+si);
		
	}

}
