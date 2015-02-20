import sqlite3

with sqlite3.connect("employees.db") as connection:
	cursor = connection.cursor()

	cursor.execute("SELECT firstname, lastname FROM employees")

	# fetchall() retrieves all records from the query
	rows = cursor.fetchall()

	# output the rows to the screen, row by row
	for r in rows:
			print r[0], r[1]
