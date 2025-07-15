import sqlite3


# your file path where you want to create a db (sql lite creates database on your local drive)
connection = sqlite3.connect(r"D:\huzair\coding\learn-sql-lite\02-sql-lite-python-connection\connection.db")

# create a cursor to interact with database
cursor = connection.cursor()

# query to create table
update_query = "update employees set name='Amir', position='CEO', salary=100000"

select_query = "select * from employees"



# executing querry
cursor.execute(update_query)

# it saves the data after insertion (updates db)
connection.commit()

# execute select query to see data
cursor.execute(select_query)

# this will return all tables in a list of tuples
print(cursor.fetchall())
