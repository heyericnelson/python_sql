import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	# drop the numbers table, if it exists
	c.execute("""DROP TABLE IF EXISTS numbers""")

	# create the table to contain the numbers
	c.execute("""CREATE TABLE numbers (number INTEGER)""")

	# create a list of 100 random numbers from 0 to 100
	numbers = random.sample(xrange(101), 100)

	# insert the numbers into the table
	c.executemany("""INSERT INTO numbers VALUES (?)""", map(lambda x: (x,), numbers))

	prompt = """What kind of calculation would you like to perform?
		    	AVG, MAX, MIN, or SUM?  Type "exit" if you would like to stop."""	
	# prompt the user for a calculation
	response = raw_input(prompt)

	# loop through until the user tells you to exit
	while response.lower() != 'exit':
		# run your query
		c.execute("""SELECT {}(number) FROM numbers""".format(response.upper()))

		# grab the result
		result = c.fetchone()

		# display the result back to the user
		print "The result of your {} operation was {}.".format(response.upper(), result[0])

		response = raw_input(prompt)
