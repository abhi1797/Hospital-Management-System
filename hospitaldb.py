

import sqlite3
con=sqlite3.connect("hospital1.db")





con.execute("CREATE TABLE hospital_table(name VARCHAR(255) not null,mobile_no bigint not null,age int not null,address VARCHAR(255) not null,DOB date not null,place VARCHAR(255) not null,pincode bigint not null)")
con.close()
