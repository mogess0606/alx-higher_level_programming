#!/usr/bin/python3

""" List all state in database """


from sys import argv 
import Mysqldb

if __name__ == '__main__':

	db_user =argv[1]
	db_passwd = argv[2]
	db_name = argv[3]

	database = MySQLdb.connect(host='localhost',
					port=3306,
					user=db_user,
					passwd=db_passwd,
					db=db_name)

	cursor = databse.cursor()

	cursor.excute('SELECT id, name FROM state ORDER By states.id ASC')

	for row in cursor.fetchall():
	print(row) 
