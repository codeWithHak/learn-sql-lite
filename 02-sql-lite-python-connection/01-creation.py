import sqlite3


# your file path where you want to create a db (sql lite creates database on your local drive)
connection = sqlite3.connect(r"D:\huzair\coding\learn-sql-lite\02-sql-lite-python-connection\connection.db")

# create a cursor to interact with database
cursor = connection.cursor()

# query to create table

create_query = "create table employees (id integer primary key autoincrement, name text, position text, salary integer)"

cursor.execute(create_query)