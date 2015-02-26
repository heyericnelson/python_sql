import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("""DROP TABLE IF EXISTS orders""")

	c.execute("""CREATE TABLE orders (make TEXT, model TEXT, order_date TEXT)""")

	orders = [
			('Honda', 'Accord', '1988-01-20'),
			('Honda', 'Accord', '2005-01-20'),
			('Honda', 'Accord', '1988-01-20'),
			('Honda', 'Civic', '1989-04-10'),
			('Honda', 'Civic', '1989-12-13'),
			('Honda', 'Civic', '1989-06-12'),
			('Ford', 'Focus', '2001-02-03'),
			('Ford', 'Focus', '2001-03-15'),
			('Ford', 'Focus', '2001-07-11'),
			('Ford', 'Mustang', '2002-05-17'),
			('Ford', 'Mustang', '2013-07-30'),
			('Ford', 'Mustang', '2010-05-19'),
			('Ford', 'Windstar', '1998-06-19'),
			('Ford', 'Windstar', '1987-10-24'),
			('Ford', 'Windstar', '2010-06-10')
					]

	c.executemany("""INSERT INTO orders VALUES (?, ?, ?)""", orders)

	c.execute("""SELECT orders.make, orders.model, orders.order_date, inventory.quantity
				FROM orders, inventory
				WHERE orders.make = inventory.make AND orders.model = inventory.model
				ORDER BY 1,2""")

	rows = c.fetchall()
	d = []

	for r in rows:
		d.append((r[0], r[1]))

	counts = {x:d.count(x) for x in d}

	for r in rows:
		print "Make & Model: " + r[0] + r[1]
		print "Inventory: " + str(r[3])
		print "Order Date: " + r[2]
