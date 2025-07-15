import sqlite3


# connect with the db
connection = sqlite3.connect(r"D:\huzair\coding\learn-sql-lite\02-sql-lite-python-connection\connection.db")

# create a cursor to interact with database
cursor = connection.cursor()

# query to data into table
select_query = "select * from employees"

# execute query
cursor.execute(select_query)

# save changes in db 
connection.commit()

# gets all the columns in an array of tuples
print(cursor.fetchall())