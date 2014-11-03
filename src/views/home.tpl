<!DOCTYPE html>
<html>
  <head>
    <title>PAAS Sample Application</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon"> 
    <link type="text/css" rel="stylesheet" href="/static/style.css">
    <link type="text/css" rel="stylesheet" href="http://cdn.datatables.net/1.10.2/css/jquery.dataTables.min.css">
    <link rel="stylesheet" href="//code.jquery.com/ui/1.11.2/themes/smoothness/jquery-ui.css">
  </head>
  <body>
 	
 	<div id="dialog-message" title="Important information">
	    <span class="ui-state-default"><span class="ui-icon ui-icon-info" style="float:left; margin:0 7px 0 0;"></span></span>
	    <div style="margin-left: 23px;">
		    First Name: <input type="text" name="fname" id="fname"><br>
		    Last Name: <input type="text" name="lname" id="lname"><br>
		    Email: <input type="text" name="email" id="email"><br> 
	    </div>
    </div>
  	<div class="container">
	    <h1>The List</h1>
	    
	    <br/>
	    
	   
	    <div class="container">
		 	<table id="userTable" class="display" cellspacing="0">
		        <thead>
		            <tr>
		            	<th></th>
		        	 	<th>First Name</th>
		                <th>Last Name</th>
		                <th>id</th>
		                <th>email</th>
		            </tr>
		        </thead>
		 
		        <tfoot>
		            <tr>
		                <th>First Name</th>
		                <th>Last Name</th>
		                <th>id</th>
		                <th>email</th>
		                <th>actions</th>              
		            </tr>
		        </tfoot>
		 
		        <tbody>
		        </tbody>
			</table>
		</div>
		<div class="sub-container">
			actions<br><hr>
			<button id="addUser">addUser</button><br>
			<button id="editUser">Edit</button><br>
			<button id="deleteUser" >Delete</button><br>
			
			   
		</div>
		
		
    </div>
	
	
	 
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
    <script type="text/javascript" src="http://cdn.datatables.net/1.10.2/js/jquery.dataTables.min.js"></script>
    <script src="//code.jquery.com/ui/1.11.2/jquery-ui.js"></script>
    <script type="text/javascript" src="/static/main.js"></script>
    
        	
   <body>
</html>
