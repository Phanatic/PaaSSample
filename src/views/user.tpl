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
  	<a href="/">back</a><br>
  	<form>
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
  		<input type="submit" value="Add"/>
%else:
	 <input type="submit" value="Edit"/>
%end
  	</form>
  </body>
</html>