import sqlite3


# your file path where you want to create a db (sql lite creates database on your local drive)
connection = sqlite3.connect(r"D:\huzair\coding\learn-sql-lite\02-sql-lite-python-connection\connection.db")

# create a cursor to interact with database
cursor = connection.cursor()

# query to create table
create_query = "create table employees (id,name,position,salary)"

# query to insert data
insert_query = "insert into employees (id,name,position,salary) values(1,'Huzair','Intern',20000), (2,'Nasir','Intern',20000)"

# query to get data
select_query = "select * from employees"




# executing querry
cursor.execute(insert_query)
# it saves the data after insertion (updates db)
connection.commit()

cursor.execute(select_query)
print(cursor.fetchall())
# this will return all tables in a list of tuples
# print(cursor.fetchall())
