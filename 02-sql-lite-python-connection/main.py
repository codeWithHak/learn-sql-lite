import sqlite3


# your file bath where you want to create a db
connection = sqlite3.connect(r"D:\huzair\coding\learn-sql-lite\02-sql-lite-python-connection\connection.db")

# create a cursor to interact with database
cursor = connection.cursor()

create_query = "create table employees (id,name,position,salary)"

insert_query = "insert into employees (id,name,position,salary) values(1,'Huzair','Intern',20000), (2,'Nasir','Intern',20000)"

select_query = "select * from employees"

delete_query = "delete from employees where id = 2"
# cursor.execute(insert_query)

# it saves the data after insertion (updates db)

cursor.execute(insert_query)
connection.commit()

cursor.execute(select_query)
# this will return all tables in a list of tuples
# print(cursor.fetchall())

# looping thorugh data (list of tuples)

data = cursor.fetchall()

for name in data:
    print(name[1])
