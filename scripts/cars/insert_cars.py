import sqlite3

with sqlite3.connect("cars.db") as connection:
	cursor = connection.cursor()

	# list out records to insert into table
	cars = [
					('Honda', 'Accord', 6),
					('Honda', 'Civic', 10),
					('Ford', 'Focus', 3),
					('Ford', 'Mustang', 1),
					('Ford', 'Windstar', 10000)
					]

	# insert records into table
	cursor.executemany("INSERT INTO inventory VALUES (?, ?, ?)", cars)

	# update the quantity on two of the records
	cursor.execute("UPDATE inventory SET quantity = 2 WHERE make = 'Honda'")

	# select all records and output them to the screen
	cursor.execute("SELECT * FROM inventory")
	rows = cursor.fetchall()

	for r in rows:
			print r[0], r[1], r[2]
	
	# select only Ford records and output them to the screen
	cursor.execute("SELECT * FROM inventory WHERE make = 'Ford'")
	rows = cursor.fetchall()

	for r in rows:
			print r[0], r[1], r[2]
