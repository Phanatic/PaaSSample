
create table  users(
	user_id mediumint(8) AUTO_INCREMENT, 
	user_fname varchar(100),
	user_lname varchar(100),
	user_email varchar(100), 
	PRIMARY	KEY(user_id),
	UNIQUE KEY user_all (user_fname,user_lname,user_email)
)