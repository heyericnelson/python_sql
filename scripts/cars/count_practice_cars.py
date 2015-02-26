import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("""SELECT orders.make, orders.model, inventory.quantity, COUNT(orders.order_date)
				 FROM orders, inventory
				 WHERE orders.make = inventory.make AND orders.model = inventory.model
				 GROUP BY 1,2,3""")

	rows = c.fetchall()

	for r in rows:
		print "Make & Model:", r[0], r[1]
		print "Inventory:", r[2]
		print "Orders:", r[3]
