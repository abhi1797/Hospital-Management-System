import sqlite3
con=sqlite3.connect("hospital1.db")
cursor=con.cursor()
'''q="select * from hospital_table "
cursor.execute(q)
result=cursor.fetchall()

print(result)
p=tuple(result)

q = "select * from hospital_table where mobile_no=8274961345"
cursor.execute(q)

result = cursor.fetchall()
print(result[0][1])
'''

q1= "select * from hospital_table where mobile_no=8274961345"
cursor.execute(q1)

result = cursor.fetchall()
print(result)
con.close()