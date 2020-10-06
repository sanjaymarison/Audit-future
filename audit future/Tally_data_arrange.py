#module to arrange rows in database according to date added
import sqlite3
from Tally_date import date,tomorrows_date

def sort_data(file):
	conn = sqlite3.connect(file)
	c = conn.cursor()

	 
	'''
	Algorithm to use*

	run all dates from year:2000 and then append every dates which have value one by one
	into the database and then evrything will be according to date order
	'''

	
	d = 1
	m = 1
	y = 2000



	date_read = str(y) + "-" + str(m) + "-" + str(d)




	list_sorted = []

	while date_read != tomorrows_date:
	#increasing the date,month and year
		d+=1
		if d == 32:
			d=1
			m+=1
		if m == 13:
			m = 1
			y +=1



		#changing the date and month from sigle digit to double digit
		if len(str(d)) == 1:
			fd = "0" + str(d)
		else:
			fd = str(d)

		if len(str(m)) == 1:
			fm = "0" + str(m)
		else:
			fm = str(m)

		date_read = str(y) + "-" + fm + "-" + fd


		c.execute("SELECT * FROM TALLY WHERE date=?",(date_read,))

		for row in c.fetchall():
			list_sorted.append(row)
		conn.commit()


	c.execute("DELETE FROM TALLY")

	for elements in list_sorted:
		c.execute('INSERT INTO TALLY (date , name , amount , category, payement, site) VALUES(?, ? ,? , ?, ?, ?)',(elements[0],elements[1],elements[2],elements[3],elements[4],elements[5]))

	conn.commit()
	conn.close()

















