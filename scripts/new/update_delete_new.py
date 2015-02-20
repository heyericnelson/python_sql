import sqlite3

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()

	# update data
	cursor.execute("UPDATE population SET population = 9000000 WHERE city = 'New York City'")

	# delete data
	cursor.execute("DELETE FROM population WHERE city = 'Boston'")

	print "\nNEW DATA:\n"

	cursor.execute("SELECT * FROM population")

	rows = cursor.fetchall()

	for r in rows:
		print r[0], r[1], r[2]
