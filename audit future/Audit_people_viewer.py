from tkinter import *
from styling import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk

def people_viewer_api():
	global img_search
	img_search = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/search.png")  # PIL solution
	img_search = img_search.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_search = ImageTk.PhotoImage(img_search)

	self_bg = "white"
	self_fg = "black"

	people_view_window = Toplevel()
	people_view_window.title("Audit viewer")
	people_view_window.state('zoomed')
	people_view_window.resizable(False,False)
	people_view_window.config(bg=self_bg)

	def remove_(entry_box):
	    entry_box.delete(0,'end')

	def search_():
		date_ = str(get_date_search.get())
		type_ = str(get_people_type_search.get())

		z = 0
		v = 0

		if date_ == "":
			date_ = "Date"
		if type_ == "":
			type_ = "People type"

		sqlite_statement = "SELECT rowid,date,peoplecount,peopletype FROM PEOPLEDATA WHERE "
		sqlite_list = []

		if date_ != "Date":
			z = 1
		if type_ != "People type":
			v = 1

		if z == 1:
			if v == 1:
				sqlite_statement = (sqlite_statement + "date=? AND peopletype=?")
				sqlite_list.append(date_)
				sqlite_list.append(type_)
			if v != 1:
				sqlite_statement = (sqlite_statement + "date=?")
				sqlite_list.append(date_)
		elif z != 1:
			if v == 1:
				sqlite_statement = (sqlite_statement + "peopletype=?")
				sqlite_list.append(type_)
			if v != 1:
				sqlite_statement = "SELECT rowid,date,peoplecount,peopletype FROM PEOPLEDATA"
		print(sqlite_statement)
		print(sqlite_list)

		tuple(sqlite_list)
		conn = sqlite3.connect(DEFAULT_PATH)
		c = conn.cursor()
		if sqlite_list == ():
			c.execute(sqlite_statement)
		else:
			c.execute(sqlite_statement,sqlite_list)

		data_display.delete(*data_display.get_children())
		for row in c.fetchall():
			data_display.insert(parent='',index='end',iid=row[0],text=row[0],values=(row[1],row[2],row[3]))


	status_viewer = Label(people_view_window)
	status_viewer.grid(row=0,column=0,columnspan=1)

	get_date_search = Entry(status_viewer,bg=self_bg,fg=self_fg,font=font,insertbackground=self_fg)
	get_date_search.grid(row=0,column=0)
	get_date_search.insert(0,"Date")
	get_date_search.bind("<Button-1>",lambda x: remove_(get_date_search))

	get_people_type_search = Entry(status_viewer,bg=self_bg,fg=self_fg,font=font,insertbackground=self_fg)
	get_people_type_search.grid(row=0,column=1)
	get_people_type_search.insert(0,"People type")
	get_people_type_search.bind("<Button-1>",lambda x: remove_(get_people_type_search))

	search_people = Button(status_viewer,bg=self_bg,fg=self_fg,font=font,image=img_search,command=search_)
	search_people.grid(row=0,column=3,columnspan=2)

	conn = sqlite3.connect(DEFAULT_PATH)
	c = conn.cursor()
	c.execute("SELECT rowid,date,peoplecount,peopletype FROM PEOPLEDATA")

	received_data = []

	data_display = ttk.Treeview(people_view_window,selectmode='browse')
	data_display['columns'] = ("Date","No of people","People category")

	data_display.column("#0",width=120,minwidth=25)
	data_display.column("Date",anchor=W,width=120,minwidth=25)
	data_display.column("No of people",anchor=W,width=120,minwidth=25)
	data_display.column("People category",anchor=W,width=120,minwidth=25)

	data_display.heading("#0",text="s.no",anchor=W)
	data_display.heading("Date",text="Date",anchor=W)
	data_display.heading("No of people",text="No of people",anchor=W)
	data_display.heading("People category",text="Category",anchor=W)


	vertical_scrollbar = ttk.Scrollbar(people_view_window,orient="vertical",command=data_display.yview)
	vertical_scrollbar.grid(row=2,column=3,sticky=N+S+E)

	data_display.configure(yscrollcommand=vertical_scrollbar.set)

	for row in c.fetchall():
	    data_display.insert(parent='',index='end',iid=row[0],text=row[0],values=(row[1],row[2],row[3]))

	data_display.grid(row=2,column=0,pady=40,columnspan=2,sticky=N+S+W+E,ipady=2)

