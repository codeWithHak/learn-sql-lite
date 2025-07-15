import sqlite3


# your file path where you want to create a db (sql lite creates database on your local drive)
connection = sqlite3.connect(r"D:\huzair\coding\learn-sql-lite\02-sql-lite-python-connection\connection.db")

# create a cursor to interact with database
cursor = connection.cursor()

# query to data into table
insert_query = "insert into employees(name, position , salary) values('Arham','Frontend Dev', 40000)"

# execute query
cursor.execute(insert_query)

# save changes in db 
connection.commit()
