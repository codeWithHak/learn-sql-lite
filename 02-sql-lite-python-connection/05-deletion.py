import sqlite3

connection = sqlite3.connect(r"D:\huzair\coding\learn-sql-lite\02-sql-lite-python-connection\connection.db")

cursor = connection.cursor()

delete_query = "drop table employees"

cursor.execute(delete_query)
