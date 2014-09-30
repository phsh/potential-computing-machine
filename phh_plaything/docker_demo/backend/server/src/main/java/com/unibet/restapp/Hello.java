package com.unibet.restapp;

import com.couchbase.client.CouchbaseClient;
import java.net.URI;
import java.util.Arrays;
import java.util.List;
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class Hello extends HttpServlet {
 
  private String errorMessage = "";
  private List<URI> hosts;
  private String bucket = "jawa-sample";
  private String password = "";
  private CouchbaseClient client;

  public void init() throws ServletException
  {
      // Do required initialization
  	try{
  	 hosts = Arrays.asList(
      new URI("http://127.0.0.1:8091/pools")
    );
      client = new CouchbaseClient(hosts, bucket, password);
    } catch(Exception e){
    	errorMessage = e.getMessage();
    	client = null;
    	throw new ServletException(e);

    }
  }

  public void doGet(HttpServletRequest request,
                    HttpServletResponse response)
            throws ServletException, IOException
  {
      
      response.setContentType("text/html");
      String paramName = "NAME";
      String paramValue = request.getParameter(paramName);
      Object data = new Object();
      if(paramValue != null){
      	if(client==null){
      		data = errorMessage;
      	}else{
      		data = client.get(paramValue);		
      	}
      	
      }
      
      // Actual logic goes here.get
      PrintWriter out = response.getWriter();

      out.println("<h1>" + data + "</h1>");
  }
  
  public void destroy()
  {
      // do nothing.
  	client.shutdown();
  }
}