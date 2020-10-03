from tkinter import *
import sqlite3
from Tally_date import date
from styling import *
from PIL import Image,ImageTk
from tkinter import ttk
from Audit_people_viewer import people_viewer_api


def advanced_data(window,window1):

	window9 = Canvas(window,bg=bg,border=0,highlightthickness=1, highlightbackground=bg)
	window9.pack(fill=BOTH,expand=True)



	label_for_date = Label(window9,text=date,bg=bg,fg=fg,font=font)
	label_for_date.grid(row=1,column=0,columnspan=1)
	label_for_date.config(font=font)


	label_for_add_todays_details = Label(window9,text="PEOPLE REPORT",bg = bg , fg= fg)
	label_for_add_todays_details.grid(row=1,column=1,padx=10,pady=10)
	label_for_add_todays_details.config(font=font)

	textbox_date = Entry(window9,width=20)
	textbox_date.grid(row=2,column=0,padx=10,pady=10)
	textbox_date.config(bg=bg,fg=fg,insertbackground=fg)
	textbox_date.insert(0,"YYYY/MM/DD")

	textbox_for_category_people = Entry(window9,width=20)
	textbox_for_category_people.grid(row=2,column=1,padx=20,pady=10)
	textbox_for_category_people.config(bg=bg,fg=fg,insertbackground=fg)
	textbox_for_category_people.insert(1,"No of people")

	

	img = Image.open(image_back)  # PIL solution
	img = img.resize((50, 50), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img = ImageTk.PhotoImage(img) # convert to PhotoImage



	def reload_second_screen():
		window9.destroy()
		advanced_data(window,window1)

	


	
	conn = sqlite3.connect(DEFAULT_PATH)
	c = conn.cursor()
	try:
		conn.execute('''CREATE TABLE IF NOT EXISTS PEOPLE(people_type TEXT)''')
	except Exception as e:
		print(e)

	c.execute('SELECT * FROM PEOPLE')
	conn.commit()

	type_people = ["Plumber","Painter"]
	for element in c.fetchall():
		type_people.append(element[0])

	def add_people():
		people_window = Toplevel()
		people_window.config(bg=window_colour)
		people_window.title("add a people category")
		

		textbox_for_category_people1 = Entry(people_window,width=20)
		textbox_for_category_people1.pack()
		textbox_for_category_people1.config(bg=bg,fg=fg,insertbackground=fg)
		textbox_for_category_people1.insert(1,"type here")

		def final_add():
			given_people = str(textbox_for_category_people1.get())
			conn = sqlite3.connect(DEFAULT_PATH)
			c = conn.cursor()
			c.execute('INSERT INTO PEOPLE (people_type) VALUES(?)',(given_people,))

			conn.commit()

			people_window.destroy()

		add_button = Button(people_window,text="ADD",bg=button_bg,fg=button_fg,font=font,command=final_add)
		add_button.pack()

	def main_screen():
		window9.destroy()
		window1()


	button_add_people = Button(window9,text="Add people type",bg=button_bg,fg=button_fg,font=font,command=add_people)
	button_add_people.grid(row=0,column=2,pady=10)

	reload_button = Button(window9,height=30,width=40,image=img,bg=button_bg,command=main_screen)
	reload_button.grid(row=0,column=0,padx=10,pady=10,sticky=W)

	view_button = Button(window9,text="View",bg=button_bg,command=people_viewer_api)
	view_button.grid(row=0,column=1,padx=10,pady=10,sticky=W)

	clicked1 = StringVar()
	chooose_option1 = ttk.Combobox(window9,textvariable=clicked1)
	chooose_option1['values'] = type_people
	chooose_option1.grid(row=2,column=2,pady=10)
	global i
	i = 0
	def add_people_report_to_database():
		global i
		conn = sqlite3.connect(DEFAULT_PATH)
		c = conn.cursor()
		try:
			conn.execute('''CREATE TABLE IF NOT EXISTS PEOPLEDATA(date TEXT,peoplecount INT,peopletype TEXT)''')
		except Exception as e:
			print(e)

		
		conn.commit()

		total_people = int(textbox_for_category_people.get())
		given_date = str(textbox_date.get())
		given_people_type = str(clicked1.get())

		if given_date == "YYYY/MM/DD":
			given_date = date


		conn.execute('INSERT INTO PEOPLEDATA(date,peoplecount,peopletype) VALUES(?,?,?)',(given_date,total_people,given_people_type,))
		conn.commit()

		i+=1

		notify_user = Label(window9,bg=button_bg,fg=button_fg,font=font,text=("Added("+str(i)+")"))
		notify_user.grid(row=4,column=2)

	button_insert_to_db = Button(window9,bg=button_bg,fg=button_fg,font=font,text="ADD",command=add_people_report_to_database)
	button_insert_to_db.grid(row=3,column=2)





	window9.mainloop()
