<!DOCTYPE html>
<html>
  <head>
    <title>PAAS Sample Application</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon"> 
    <link type="text/css" rel="stylesheet" href="/static/style.css">
    <link type="text/css" rel="stylesheet" href="http://cdn.datatables.net/1.10.2/css/jquery.dataTables.min.css">
  </head>
  <body>
  	<div>Hello!!</div>
    <div>
 	<table id="userTable" class="display" cellspacing="0" width="100%">
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
            </tr>
        </tfoot>
 
        <tbody>
        </tbody>
	</table>
	<div>
	<div>
	
	<button id="addUser">addUser</button><br>
	<button id="editUser">Edit</button><br>
	<button id="deleteUser" >Delete</button><br>
	
	</div>
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
    <script type="text/javascript" src="http://cdn.datatables.net/1.10.2/js/jquery.dataTables.min.js"></script>
    <script type="text/javascript" src="/static/main.js"></script>
    
    
   <body>
</html>
