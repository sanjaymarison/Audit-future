import sqlite3
from styling import DEFAULT_PATH

def refresh():
	conn = sqlite3.connect(DEFAULT_PATH)
	c = conn.cursor()

	c.execute("SELECT * FROM TALLY")

	data = []

	for row in c.fetchall():
		data.append(row)

	c.execute("DELETE FROM TALLY")

	conn.commit()

	conn.execute('''CREATE TABLE IF NOT EXISTS TALLY(date TEXT,
	                                                name TEXT,
	                                                amount INT,
	                                                category TEXT,
	                                                payement TEXT,
	                                                site TEXT,
	                                                time TEXT)''')
	print(data)

	for value in data:
		print(value)
		tup = (value[0],value[1],value[2],value[3],value[4],value[5],value[6])
		c.execute('INSERT INTO TALLY (date , name , amount , category, payement, site,time) VALUES(?, ? ,? , ?, ?, ?, ?)',tup)
	conn.commit()