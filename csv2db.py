import sys
import csv
import MySQLdb

if __name__ == "__main__":
	db = MySQLdb.connect(host="localhost",
				user="root",
				passwd="",
				db="test")

	cur = db.cursor()

	with open('test.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
		
		for row in reader:
			#print ', '.join(row)
			
			cur.execute("INSERT INTO table (Col1, Col2 ...) VALUES (%s);" % 
									', '.join(row)) 
