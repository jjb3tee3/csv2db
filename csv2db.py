from subprocess import call
import csv
import MySQLdb

"""
Need to determine what the .vif input files are named
and what the resulting .csv is named.
"""
def get_csv():
	call(["vif2csv", ""])

"""
Removes the CSV files once the action has been completed.
"""
def remove_csv():
	call(["rm", "*.csv"])

if __name__ == "__main__":
	db = MySQLdb.connect(host="localhost",
				user="root",
				passwd="",
				db="test")
	foundRow = false
	cur = db.cursor()

	get_csv()
	
	# dbrow = cur.execute(<select last row query here>)

	with open('test.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
		
		for row in reader:
			# Check first so the same row isn't entered twice when found
			if found:
				cur.execute("INSERT INTO table (Col1, Col2 ...) VALUES (%s);" % 
									', '.join(row))
			# Trying to identify the last row we synced
			if ''.join(dbrow) == ''.join(row):
				found = true

	remove_csv()
