create table users( 
user_id int not null auto_increment, 
user_fname varchar(100) NOT NULL, 
user_lname varchar(100) NOT NULL, 
user_email varchar(100),
create_date DATE, 
PRIMARY KEY(user_id),
UNIQUE(user_fname,user_lname,user_email)
)

