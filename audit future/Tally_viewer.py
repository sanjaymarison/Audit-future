from tkinter import Label,Button,Entry,Tk,W,S,E,N,LabelFrame,StringVar,DISABLED
from tkinter import ttk
from tkinter import filedialog
from styling import *
import sqlite3
from Tally_data_arrange import sort_data
from Tally_backup import create_backup
import threading
import string
import time
from Tally_excel_sheet import export_window
from Audit_send_record import send_record

def viewer_api(date1="Date",name1="Name",category1="Category",payement1="Payement",site1="Site",amount1="Amount",file=DEFAULT_PATH):
	def backup_():
		file_name = filedialog.askopenfilename(initialdir=str(backup_path),title="Select backup file")
		if file_name != "":
			window_viewer.destroy()
			viewer_api(file=str(file_name))

	def change_file_():
		file_name_ = filedialog.askopenfilename(title="Select file to open")
		if file_name_ != "":
			window_viewer.destroy()
			viewer_api(file=str(file_name_))
	print(file)
	z = 0

	if date1 == "":
		date1 = "Date"
	if name1 == "":
		name1 = "Name"
	if category1 == "":
		category1 = "Category"
	if payement1 == "":
		payement1 = "Payement"
	if site1 == "":
		site1 = "Site"
	if amount1 == "":
		amount1 = "Amount"


	if date1 != "Date":
		z = 1
	if name1 != "Name":
		z = 1
	if category1 != "Category":
		z = 1
	if payement1 != "Payement":
		z = 1
	if site1 != "Site":
		z = 1
	if amount1 != "Amount":
		z = 1
	def search_api():
		date_viewer_search = str(date_viewer.get())
		name_viewer_search = str(name_viewer.get())
		amount_viewer_search = str(amount_viewer.get())
		payement_viewer_search = str(payement_viewer.get())
		site_viewer_search = str(site_viewer.get())
		category_viewer_search = str(category_viewer.get())


		if date_viewer_search == "":
			date_viewer_search = "Date"
		if name_viewer_search == "":
			name_viewer_search = "Name"
		if category_viewer_search == "":
			category_viewer_search = "Category"
		if payement_viewer_search == "":
			payement_viewer_search = "Payement"
		if site_viewer_search == "":
			site_viewer_search = "Site"
		if amount_viewer_search == "":
			amount_viewer_search = "Amount"


		sqlite_statement = "SELECT * FROM TALLY WHERE "
		sqlite_list = []

		if date_viewer_search != "Date":
		    if sqlite_statement == "SELECT * FROM TALLY WHERE ":
		        sqlite_statement = sqlite_statement + "date=?"
		    else:
		        sqlite_statement = sqlite_statement + " AND date=?"
		    sqlite_list.append(date_viewer_search)

		if name_viewer_search != "Name":
		    if sqlite_statement == "SELECT * FROM TALLY WHERE ":
		        sqlite_statement = sqlite_statement + "name=?"
		    else:
		        sqlite_statement = sqlite_statement + " AND name=?"
		    sqlite_list.append(name_viewer_search)

		if amount_viewer_search != "Amount":
		    if sqlite_statement == "SELECT * FROM TALLY WHERE ":
		        sqlite_statement = sqlite_statement + "amount=?"
		    else:
		        sqlite_statement = sqlite_statement + " AND amount=?"
		    sqlite_list.append(amount_viewer_search)

		if category_viewer_search != "Category":
		    if sqlite_statement == "SELECT * FROM TALLY WHERE ":
		        sqlite_statement = sqlite_statement + "category=?"
		    else:
		        sqlite_statement = sqlite_statement + " AND category=?"
		    sqlite_list.append(category_viewer_search)

		if payement_viewer_search != "Payement":
		    if sqlite_statement == "SELECT * FROM TALLY WHERE ":
		        sqlite_statement = sqlite_statement + "payement=?"
		    else:
		        sqlite_statement = sqlite_statement + " AND payement=?"
		    sqlite_list.append(payement_viewer_search)

		if site_viewer_search != "Site":
		    if sqlite_statement == "SELECT * FROM TALLY WHERE ":
		        sqlite_statement = sqlite_statement + "site=?"
		    else:
		        sqlite_statement = sqlite_statement + " AND site=?"
		    sqlite_list.append(site_viewer_search)

		tuple(sqlite_list)
		if sqlite_statement == "SELECT * FROM TALLY WHERE ":
			sqlite_statement = "SELECT * FROM TALLY"
		c.execute(sqlite_statement,sqlite_list)
		column_s_no = 0
		total_amount = []
		my_tree.delete(*my_tree.get_children())
		for row in c.fetchall():
			column_s_no += 1
			my_tree.insert(parent='',index='end',iid=(column_s_no-1),text=column_s_no,values=(row[0],row[1],row[3],row[4],row[5],row[2]))
			total_amount.append(row[2])
		label_total.config(text=str("Total amount:" + str(sum(total_amount))))

	conn = sqlite3.connect(file)
	c = conn.cursor()
	c.execute("SELECT * FROM TALLY")

	window_viewer = Tk()
	window_viewer.title("Audit viewer")
	window_viewer.state("zoomed")
	window_viewer.resizable(False,False)

	status_viewer = Label(window_viewer)
	status_viewer.grid(row=0,column=0,columnspan=1)

	date_viewer = Entry(status_viewer)
	date_viewer.grid(row=0,column=0)
	date_viewer.insert(0,date1)

	name_viewer = Entry(status_viewer)
	name_viewer.grid(row=0,column=1)
	name_viewer.insert(0,name1)

	amount_viewer = Entry(status_viewer)
	amount_viewer.grid(row=0,column=2)
	amount_viewer.insert(0,amount1)

	category_viewer = Entry(status_viewer)
	category_viewer.grid(row=0,column=3)
	category_viewer.insert(0,category1)

	payement_viewer = Entry(status_viewer)
	payement_viewer.grid(row=0,column=4)
	payement_viewer.insert(0,payement1)

	site_viewer = Entry(status_viewer)
	site_viewer.grid(row=0,column=5)
	site_viewer.insert(0,site1)

	def sort_data_and_destroy(file):
		window_viewer.destroy()
		sort_data(file)
		viewer_api()


	def reset():
		def reset_confirm():
			window_viewer.destroy()
			conn = sqlite3.connect(DEFAULT_PATH)
			c = conn.cursor()
			c.execute("DELETE FROM TALLY")
			conn.commit()
			viewer_api()


		response = messagebox.askyesno("RESET","Are you sure you want to reset? (YOU CANT UNDO THIS)")
		if response == 1:
			reset_confirm()
		elif response== 0:
			pass



	search_viewer = Button(status_viewer,text="Search",width=20,command=search_api)
	search_viewer.grid(row=1,column=2,columnspan=2,sticky=W+E)

	my_tree = ttk.Treeview(window_viewer,selectmode='browse')

	#defining columns
	my_tree['columns'] = ("Date","Name","Category","Payement","Site","Amount")


	#format our columns
	my_tree.column("#0",width=120,minwidth=25)
	my_tree.column("Date",anchor=W,width=120,minwidth=25)
	my_tree.column("Name",anchor=W,width=120,minwidth=25)
	my_tree.column("Category",anchor=W,width=120,minwidth=25)
	my_tree.column("Payement",anchor=W,width=120,minwidth=25)
	my_tree.column("Site",anchor=W,width=120,minwidth=25)
	my_tree.column("Amount",anchor=W,width=120,minwidth=25)

	#create headings
	my_tree.heading("#0",text="s.no",anchor=W)
	my_tree.heading("Date",text="Date",anchor=W)
	my_tree.heading("Name",text="Name",anchor=W)
	my_tree.heading("Category",text="Category",anchor=W)
	my_tree.heading("Payement",text="Payement",anchor=W)
	my_tree.heading("Site",text="Site",anchor=W)
	my_tree.heading("Amount",text="Amount",anchor=W)


	vertical_scrollbar = ttk.Scrollbar(window_viewer,orient="vertical",command=my_tree.yview)
	vertical_scrollbar.grid(row=2,column=0,sticky=N+S+E)

	my_tree.configure(yscrollcommand=vertical_scrollbar.set)

	def selected_option_delete():
		try:
			x =  my_tree.selection()
			for selected in x:
				my_tree.delete(selected)
				print(selected)
				conn = sqlite3.connect(file)
				c = conn.cursor()
				selected_ = int(selected) + 1
				c.execute("DELETE FROM TALLY WHERE rowid=?",(selected_,))
			conn.commit()
		except:
			print("User is clicking delete without choosing an option")


	def selected_option_edit():
		#chooses wrong option some times might be buggy 
		#Not recommended for use
		def edit_():
			pass

		ask_new_values = Tk()
		ask_new_values.title("Edit")
		ask_new_values.resizable(False,False)
		label_say = Label(ask_new_values,text="Enter new values")
		label_say.pack()
		date_edit = Entry(ask_new_values,font=font)
		date_edit.pack()
		name_edit = Entry(ask_new_values,font=font)
		name_edit.pack()
		amount_edit = Entry(ask_new_values,font=font)
		amount_edit.pack()
		site_edit = Entry(ask_new_values,font=font)
		site_edit.pack()
		options = StringVar()
		category_edit = Entry(ask_new_values,font=font)
		category_edit.pack()
		payement_edit = ttk.Combobox(ask_new_values,textvariable=options)
		payement_edit['values'] = ("Credited","Debited","select")
		payement_edit.config(width=15)
		

		x =  my_tree.selection()
		print(x)

		for num in x:
			conn = sqlite3.connect(file)
			c = conn.cursor()
			print(int(num))
			num_ = int(num)+1
			print(num_)
			c.execute("SELECT * FROM TALLY WHERE rowid=?",(num_,))
			print(c.fetchall())
			for row in c.fetchall():
				print(row)
				date_edit.insert(0,row[0])
				name_edit.insert(0,row[1])
				amount_edit.insert(0,row[2])
				site_edit.insert(0,row[5])
				category_edit.insert(0,row[3])
				if str(row[4]) == "Credited":
					payement_edit.current(0)
				else:
					payement_edit.current(1)
				print(row[4])

		payement_edit.pack()
		button_edit = Button(ask_new_values,text="Edit",command=edit_)
		button_edit.pack()
		ask_new_values.mainloop()

	#add data
	column_s_no = 0
	total_amount = []

	for row in c.fetchall():
		column_s_no += 1
		my_tree.insert(parent='',index='end',iid=(column_s_no-1),text=column_s_no,values=(row[0],row[1],row[3],row[4],row[5],row[2]))
		total_amount.append(row[2])

	my_tree.grid(row=2,column=0,pady=40,sticky=N+S+W+E,ipady=2)
	
	label_total = Label(window_viewer,font=font,text=str("Total amount:" + str(sum(total_amount))))
	label_total.grid(row=3,column=0)

	data_tools = LabelFrame(window_viewer,border=5)
	data_tools.grid(row=4,column=0,columnspan=1)

	reset_button = Button(data_tools,width=b_wd,text="RESET",command=reset)
	reset_button.grid(row=0,column=0,pady=10)
	reset_button.config(bg=button_bg,fg=button_fg,font=font)

	sort_data_button = Button(data_tools,bg=button_bg,fg=button_fg,font=font,text="Sort data",command=lambda: sort_data_and_destroy(file))
	sort_data_button.grid(row=0,column=1,sticky=W+E)

	change_file = Button(data_tools,bg=button_bg,fg=button_fg,font=font,text="Change file",command=change_file_)
	change_file.grid(row=0,column=2,sticky=W+E)

	open_backup = Button(data_tools,bg=button_bg,fg=button_fg,font=font,text="Open Backup",command=backup_)
	open_backup.grid(row=0,column=3,sticky=W+E)

	delete_record = Button(data_tools,bg=button_bg,fg=button_fg,font=font,text="Delete",command=selected_option_delete)
	delete_record.grid(row=0,column=4,sticky=W+E)

	edit_record = Button(data_tools,bg=button_bg,fg=button_fg,font=font,text="Edit",command=selected_option_edit,state=DISABLED)
	edit_record.grid(row=0,column=5,sticky=W+E)

	export_record = Button(data_tools,bg=button_bg,fg=button_fg,font=font,text="Export record",command=export_window)
	export_record.grid(row=0,column=6,sticky=W+E)

	backup_record = Button(data_tools,bg=button_bg,fg=button_fg,font=font,text="Backup record",command=create_backup)
	backup_record.grid(row=0,column=7,sticky=W+E)

	send_record_ = Button(data_tools,bg=button_bg,fg=button_fg,font=font,text="Send record",command=send_record)
	send_record_.grid(row=0,column=8,sticky=W+E)



	if z == 1:
		search_api()

	window_viewer.mainloop()
