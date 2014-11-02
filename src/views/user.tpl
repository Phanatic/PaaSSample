<!DOCTYPE html>
<html>
  <head>
    <title>PAAS Sample Application Add User dialog</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon"> 
    <link type="text/css" rel="stylesheet" href="/static/style.css">
    <link type="text/css" rel="stylesheet" href="http://cdn.datatables.net/1.10.2/css/jquery.dataTables.min.css">
  </head>
  <body>
  <div class="container">
  	<a href="/">back</a><br>
  	<form class="sub-container">
%if fname != None:
  		First Name: <input type="text" name="fname" value="{{fname}}"/><br>
%else:
		First Name: <input type="text" name="fname"><br>
%end
%if lname != None:
  		Last Name: <input type="text" name="lname" value="{{lname}}"/><br>
%else:
		Last Name: <input type="text" name="lname"><br>
%end
%if email != None:
  		Email: <input type="text" name="email" value="{{email}}"/><br>
%else:
		Email: <input type="text" name="email"><br>
%end
%if action == 'add':
  		<input id="addUser" type="submit" value="Add"/>
%else:
	 <input id="edit" type="submit" value="Edit"/>
%end
  	</form>
  	</div>
  	
  	<script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
    <script type="text/javascript" src="http://cdn.datatables.net/1.10.2/js/jquery.dataTables.min.js"></script>
    <script src="//code.jquery.com/ui/1.11.2/jquery-ui.js"></script>
    <script type="text/javascript" src="/static/useradd.js"></script>
  </body>
</html>