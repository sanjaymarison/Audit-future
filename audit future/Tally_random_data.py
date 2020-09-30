import sqlite3
import random
import string
import os

def random_g(user_input):
	list_to_add = []
	for z in range(user_input):
		letters = string.ascii_letters
		letters = ''.join(random.choice(letters) for i in range(random.randint(1,10))) 

		letter1 = string.ascii_letters
		letter1 = ''.join(random.choice(letters) for i in range(random.randint(1,10))) 

		amount_random = random.randint(1000,5000000)
		name_random = letters
		site_random = random.randint(1,30)
		category_random = letter1
		list_payement = ["Credited","Debited"]
		type_random = random.choice(list_payement)
		month_s = str(random.randint(1,12))
		date_s = str(random.randint(1,31))
		if len(month_s) == 1:
			month_s = "0" + month_s
		if len(date_s) == 1:
			date_s = "0" + date_s

		date_random = str(random.randint(2000,2020)) + "-" + month_s + "-" + date_s
		list_to_add.append([date_random,name_random,amount_random,category_random,type_random,site_random])



	DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'appdata.db')
	conn = sqlite3.connect(DEFAULT_PATH)
	c = conn.cursor()
	conn.execute('''CREATE TABLE IF NOT EXISTS TALLY(date TEXT,
	                                                 name TEXT,
	                                                 amount INT,
	                                                 category TEXT,
	                                                 payement TEXT,
	                                                 site TEXT)''')
	for items in list_to_add:
		print(items)
		c.execute('INSERT INTO TALLY (date , name , amount , category, payement, site) VALUES(?, ? ,? , ?, ?, ?)',(items[0],items[1],items[2],items[3],items[4],items[5]))
	conn.commit()