import sqlite3


# your file bath where you want to create a db
connection = sqlite3.connect(r"D:\huzair\coding\learn-sql-lite\02-sql-lite-python-connection\connection.db")

cursor = connection.cursor()

create_query = "create table employees (id,name,position,salary)"

insert_query = "insert into employees (id,name,position,salary) values(1,'Huzair','Intern',20000), (2,'Nasir','Intern',20000)"

select_query = "select * from employees"

cursor.execute(insert_query)
connection.commit()


cursor.execute(select_query)

print(cursor.fetchall())