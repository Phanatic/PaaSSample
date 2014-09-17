// main.js


        
$(document).ready(function() {
	var t = $('#userTable').DataTable();
	//TODO: make an ajax call to host (TODO: how to get URL injected here? domain name?)
	$.get('/getusers',function(data, status) {
		console.log(data);
		var obj = $.parseJSON(data);
		
		$.each(obj, function() {
			var strStart = '<input type="radio" name="user" value="';
			var strEnd = '"/>';
			var checkBoxStr = strStart + this['id']+strEnd;
			t.row.add([checkBoxStr,this['fname'],this['lname'],this['id'],this['email']]).draw();
			});
					
	});
	
	console.log("ready")
});

$("#addUser").click(function() {
	alert("clicked add!");
	window.location.href = '/userForm/add';
});

$("#editUser").click(function(){
	// find the selected radio button in the table.
	
	var userid = $('input[name=user]:checked').val();
	if(typeof userid  == 'undefined') {
		alert("please select a user to edit");
	}
	else {
		var hrefstr = 'userForm/edit?userid='+userid;
		window.location.href = hrefstr ;
	}
	});

$("#deleteUser").click(function() {
	var userid = $('input[name=user]:checked').val();
	if(typeof userid  == 'undefined') {
		alert("please select a user to delete");
	}
	else {
		var hrefstr = '/deleteuser/'+userid;
		$.ajax( {
			url: hrefstr,
			type:'DELETE',
			success: function(result) {
				alert("successfully deleted "+userid);
			}
		});
		location.reload(true);
		
	}

	});