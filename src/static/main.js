// main.js


        
$(document).ready(function() {
	var t = $('#userTable').DataTable();
	$("#dialog-message").hide();
	$.get('/getusers',function(data, status) {
		console.log(data);
		var obj = $.parseJSON(data);
		
		$.each(obj, function() {
			var strStart = '<input type="radio" name="user" value="';
			var strEnd = '"/>';
			var checkBoxStr = strStart + this['id']+strEnd;
			var linkstr = '<a href="/adduser/">adduser</a>'
			t.row.add([checkBoxStr,this['fname'],this['lname'],this['id'],this['email']]).draw();
			});
					
	});
	
	console.log("ready")
});



$("#addUser").click(function() {
	window.location.href = '/userForm/add';
	
	/*$("#dialog-message").dialog({
	    modal: true,
	    draggable: false,
	    resizable: false,
	    show: 'blind',
	    hide: 'blind',
	    width: 400,
	    dialogClass: 'container',
	    buttons: {
		        "Add": function() {
		        	$.post('/userform/add')
		            $(this).dialog("close");
		        }
		    }
		});
		
	$("#dialog-message").show();
	*/
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