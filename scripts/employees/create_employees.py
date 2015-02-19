import csv
import sqlite3

with sqlite3.connect("employees.db") as connection:
	c = connection.cursor()

	# open the csv file and assign it to a variable
	employees = csv.reader(open("employees.csv","rU"), delimiter = '\t')

	# create a new table called employees
	c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

	# insert data into table
	c.executemany("INSERT INTO employees(firstname, lastname) VALUES (?, ?)", employees)
