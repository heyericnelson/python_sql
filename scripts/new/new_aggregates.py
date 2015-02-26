import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# create a dictionary of SQL queries
	sql = {'average': "SELECT AVG(population) FROM population",
		   'maximum': "SELECT MAX(population) FROM population",
		   'minimum': "SELECT MIN(population) FROM population",
		   'sum': "SELECT SUM(population) FROM population",
		   'count': "SELECT COUNT(city) FROM population"}

	# run each SQL query item in the dictionary
	for key, value in sql.iteritems():

			# run SQL
			c.execute(value)

			# fetchone() retrieves one record from the query
			result = c.fetchone()

			# output the result to screen
			print key + ":", result[0]
