import os 
import sqlite3
import matplotlib.pyplot as plt
from Tally_date import tomorrows_date
from tkinter import messagebox
import time



def graph(payement_type_=None):	
	messagebox.showinfo("Reading data","This might take some time depending on size of data , click ok to continue")
	time.sleep(2)
	DEFAULT_PATH = os.path.join(os.path.dirname(__file__),'appdata.db')
	conn = sqlite3.connect(DEFAULT_PATH)
	c = conn.cursor()


	pt = payement_type_

	global y,m,d
	y = 2000
	m = 1
	d = 1

	cc = str(y) + "-"  + str(m) + "-" + str(d)

	amount = []
	list_to_graph = []
	one_axis_x = []
	one_axis_y = []



	while cc != tomorrows_date:
		c.execute("SELECT * FROM TALLY WHERE date=? AND payement=?",(cc,pt,))

		for row in c.fetchall():
			amount.append(row[2])
		a = sum(amount)


		if a == 0 :
			amount.clear()

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

			cc = str(y) + "-" + fm + "-" + fd

		elif a != 0 :
			list_to_graph.append([cc,a])
			amount.clear()

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

			cc = str(y) + "-" + fm + "-" + fd
			print(cc)


	print("appending")
	for elements in list_to_graph:
		one_axis_x.append(elements[0])
		one_axis_y.append(elements[1])
	plt.plot(one_axis_x,one_axis_y)
	plt.xticks(rotation=90)
	messagebox.showinfo("Plotting","Data has been processed ,plotting has started")
	time.sleep(2)
	plt.show()

def total_graph():
	DEFAULT_PATH = os.path.join(os.path.dirname(__file__),'appdata.db')
	conn = sqlite3.connect(DEFAULT_PATH)
	c = conn.cursor()


	pt_1 = "Debited"
	pt_2 = "Credited"

	global y,m,d
	y = 2000
	m = 1
	d = 1

	cc = str(y) + "-"  + str(m) + "-" + str(d)

	amount = []
	amount1 = []
	list_to_graph = []
	one_axis_x = []
	one_axis_y = []



	while cc != tomorrows_date:
		c.execute("SELECT * FROM TALLY WHERE date=? AND payement=?",(cc,pt_1,))

		for row in c.fetchall():
			amount.append(row[2])
		a = sum(amount)

		c.execute("SELECT * FROM TALLY WHERE date=? AND payement=?",(cc,pt_2,))

		for row in c.fetchall():
			amount1.append(row[2])
		a1 = sum(amount1)

		final_a = a1 - a

		if a == 0:
			if a1 == 0:
				amount.clear()
				amount1.clear()

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

				cc = str(y) + "-" + fm + "-" + fd

		if a != 0:
			list_to_graph.append([cc,final_a])
			amount.clear()
			amount1.clear()

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

			cc = str(y) + "-" + fm + "-" + fd
		if a1 != 0:
			list_to_graph.append([cc,final_a])
			amount.clear()
			amount1.clear()

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

			cc = str(y) + "-" + fm + "-" + fd

	for elements in list_to_graph:
		one_axis_x.append(elements[0])
		one_axis_y.append(elements[1])

	c.close()
	conn.close()

	plt.plot(one_axis_x,one_axis_y)
	plt.xticks(rotation=90)
	plt.show()
	

	





