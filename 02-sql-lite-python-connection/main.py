import sqlite3


# your file bath where you want to create a db
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

# this will return all tables in a list of tuples
# print(cursor.fetchall())


# looping thorugh data (list of tuples)
data = cursor.fetchall()

for name in data:
    print(name[1])







# -------------- More Queries --------------------



# query to delete table
delete_table_query = "drop table employees"

# query to delete data
delete_data_query = "delete from employees where id = 2"

# query to delete data
delete_column_query = "delete from employees where id = 2"
