from tkinter import *
from tkinter import ttk,filedialog
from styling import *
import sqlite3
from Tally_data_arrange import sort_data
from Tally_backup import create_backup
import threading
import string
import time
from Tally_excel_sheet import export_window
from Audit_send_record import send_record
from refresh_database import refresh
from PIL import ImageTk,Image
from babel.numbers import format_currency

def viewer_api(date1="Date",name1="Name",category1="Category",payement1="Payement",site1="Site",amount1="Amount",file=DEFAULT_PATH):
	def format_num(value):
		amount = format_currency(value, 'INR', locale='en_IN')
		return amount
	global img_search
	img_search = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/search.png")  # PIL solution
	img_search = img_search.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_search = ImageTk.PhotoImage(img_search)

	global img_add
	img_add = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/add.png")  # PIL solution
	img_add = img_add.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_add = ImageTk.PhotoImage(img_add)

	global img_upload
	img_upload = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/upload.png")  # PIL solution
	img_upload = img_upload.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_upload = ImageTk.PhotoImage(img_upload)

	global img_info
	img_info = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/info.png")
	img_info = img_info.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_info = ImageTk.PhotoImage(img_info)

	global img_help
	img_help = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/help.png")
	img_help = img_help.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_help = ImageTk.PhotoImage(img_help)

	global img_mail
	img_mail = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/mail.png")
	img_mail = img_mail.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_mail = ImageTk.PhotoImage(img_mail)

	global img_sort
	img_sort = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/sort.png")
	img_sort = img_sort.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_sort = ImageTk.PhotoImage(img_sort)

	global img_delete
	img_delete = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/delete.png")  
	img_delete = img_delete.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_delete = ImageTk.PhotoImage(img_delete)

	global img_reset
	img_reset = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/reset.png")  
	img_reset = img_reset.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_reset = ImageTk.PhotoImage(img_reset)

	global img_edit
	img_edit = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/edit.png")  
	img_edit = img_edit.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_edit = ImageTk.PhotoImage(img_edit)

	global img_choose_file
	img_choose_file = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/choose_file.png")  
	img_choose_file = img_choose_file.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_choose_file = ImageTk.PhotoImage(img_choose_file)

	global img_choose_backup
	img_choose_backup = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/choose_backup.png")  
	img_choose_backup = img_choose_backup.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_choose_backup = ImageTk.PhotoImage(img_choose_backup)

	global img_export
	img_export = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/export.png")  
	img_export = img_export.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_export = ImageTk.PhotoImage(img_export)

	global img_backup
	img_backup = Image.open("/Users/sanjaymarison/Library/Mobile Documents/com~apple~CloudDocs/Audit future/audit future/Resources/backup.png")  
	img_backup = img_backup.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img_backup = ImageTk.PhotoImage(img_backup)


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


		sqlite_statement = "SELECT rowid,* FROM TALLY WHERE "
		sqlite_list = []

		if date_viewer_search != "Date":
		    if sqlite_statement == "SELECT rowid,* FROM TALLY WHERE ":
		        sqlite_statement = sqlite_statement + "date=?"
		    else:
		        sqlite_statement = sqlite_statement + " AND date=?"
		    sqlite_list.append(date_viewer_search)

		if name_viewer_search != "Name":
		    if sqlite_statement == "SELECT rowid,* FROM TALLY WHERE ":
		        sqlite_statement = sqlite_statement + "name=?"
		    else:
		        sqlite_statement = sqlite_statement + " AND name=?"
		    sqlite_list.append(name_viewer_search)

		if amount_viewer_search != "Amount":
		    if sqlite_statement == "SELECT rowid,* FROM TALLY WHERE ":
		        sqlite_statement = sqlite_statement + "amount=?"
		    else:
		        sqlite_statement = sqlite_statement + " AND amount=?"
		    sqlite_list.append(amount_viewer_search)

		if category_viewer_search != "Category":
		    if sqlite_statement == "SELECT rowid,* FROM TALLY WHERE ":
		        sqlite_statement = sqlite_statement + "category=?"
		    else:
		        sqlite_statement = sqlite_statement + " AND category=?"
		    sqlite_list.append(category_viewer_search)

		if payement_viewer_search != "Payement":
		    if sqlite_statement == "SELECT rowid,* FROM TALLY WHERE ":
		        sqlite_statement = sqlite_statement + "payement=?"
		    else:
		        sqlite_statement = sqlite_statement + " AND payement=?"
		    sqlite_list.append(payement_viewer_search)

		if site_viewer_search != "Site":
		    if sqlite_statement == "SELECT rowid,* FROM TALLY WHERE ":
		        sqlite_statement = sqlite_statement + "site=?"
		    else:
		        sqlite_statement = sqlite_statement + " AND site=?"
		    sqlite_list.append(site_viewer_search)

		tuple(sqlite_list)
		if sqlite_statement == "SELECT rowid,* FROM TALLY WHERE ":
			sqlite_statement = "SELECT rowid,* FROM TALLY"
		c.execute(sqlite_statement,sqlite_list)
		column_s_no = 0
		total_amount = []
		data_table.delete(*data_table.get_children())
		for row in c.fetchall():
			column_s_no += 1
			data_table.insert(parent='',index='end',iid=row[0],text=row[0],values=(row[1],row[2],row[4],row[5],row[6],format_num(row[3])))
			total_amount.append(row[3])
		label_total.config(text=str("Total amount:" + format_num(str(sum(total_amount)))))

	conn = sqlite3.connect(file)
	c = conn.cursor()
	c.execute("SELECT rowid,* FROM TALLY")

	window_viewer = Toplevel()
	window_viewer.title("Audit viewer")
	window_viewer.state("normal")
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
		sort_data(file)
		search_api()


	def reset():
		def reset_confirm():
			conn = sqlite3.connect(file)
			c = conn.cursor()
			c.execute("DELETE FROM TALLY")
			conn.commit()
			search_api()


		response = messagebox.askyesno("RESET","Are you sure you want to reset? (YOU CANT UNDO THIS)")
		if response == 1:
			reset_confirm()
		elif response== 0:
			pass

	
	search_viewer = Button(status_viewer,image=img_search,command=search_api,borderwidth=0,bd=0)
	search_viewer.grid(row=0,column=6)

	frame_button = Frame(status_viewer)
	frame_button.grid(row=1,column=4,columnspan=3,ipady=0)


	'''
	style for data_table unofficial
		style = ttk.Style()
		style.theme_use('clam')
		style.configure('Treeview',
	88464099842  271158		background='#D3D3D3',
			foreground='black',
			rowheight=50,
			row=20,
			fieldbackground='#D3D3D3')
		style.map('Treeview',
			background=[('selected','blue')])
	'''

	data_table = ttk.Treeview(window_viewer,selectmode='browse')

	#defining columns
	data_table['columns'] = ("Date","Name","Category","Payement","Site","Amount")


	#format our columns
	data_table.column("#0",width=120,minwidth=25)
	data_table.column("Date",anchor=W,width=120,minwidth=25)
	data_table.column("Name",anchor=W,width=120,minwidth=25)
	data_table.column("Category",anchor=W,width=120,minwidth=25)
	data_table.column("Payement",anchor=W,width=120,minwidth=25)
	data_table.column("Site",anchor=W,width=120,minwidth=25)
	data_table.column("Amount",anchor=W,width=120,minwidth=25)

	#create headings
	data_table.heading("#0",text="rowid",anchor=W)
	data_table.heading("Date",text="Date",anchor=W)
	data_table.heading("Name",text="Name",anchor=W)
	data_table.heading("Category",text="Category",anchor=W)
	data_table.heading("Payement",text="Payement",anchor=W)
	data_table.heading("Site",text="Site",anchor=W)
	data_table.heading("Amount",text="Amount",anchor=W)


	vertical_scrollbar = ttk.Scrollbar(window_viewer,orient="vertical",command=data_table.yview)
	vertical_scrollbar.grid(row=2,column=0,sticky=N+S+E)

	data_table.configure(yscrollcommand=vertical_scrollbar.set)

	def selected_option_delete():
		try:
			x =  data_table.selection()
			for selected in x:
				data_table.delete(selected)
				print(selected)
				conn = sqlite3.connect(file)
				c = conn.cursor()
				selected_ = int(selected) + 1
				c.execute("DELETE FROM TALLY WHERE rowid=?",(selected_,))
			conn.commit()
			refresh()
			search_api()
		except:
			print("User is clicking delete without choosing an option")


	def selected_option_edit():
		def edit_(num_):
			date = str(date_edit.get())
			name = str(name_edit.get())
			amount = str(amount_edit.get())
			site = str(site_edit.get())
			category = str(category_edit.get())
			option = str(options.get())
			num = str(num_)
			statement = f'UPDATE TALLY SET name = "{name}" , date = "{date}" , amount = "{amount}" , site = "{site}" , category = "{category}" , payement = "{option}" WHERE rowid = "{num}"'
			print(statement)
			c.execute(statement)
			conn.commit()
			search_api()
			ask_new_values.destroy()
		x =  data_table.selection()
		print(x)

		num = x[0]
		conn = sqlite3.connect(file)
		c = conn.cursor()
		num_ = num
		c.execute("SELECT * FROM TALLY WHERE rowid=?",(num_,))
		
		for row in c.fetchall():
			print(row)
			date = row[0]
			name = row[1]
			amount = row[2]
			site = row[5]
			category = row[3]
			if str(row[4]) == "Credited":
				payement = 0
			else:
				payement = 1
		#chooses wrong option some times might be buggy 
		#Not recommended for use

		ask_new_values = Toplevel()
		ask_new_values.title("Edit")
		ask_new_values.resizable(False,False)

		label_say = Label(ask_new_values,text="Enter new values")
		label_say.pack()

		date_edit = Entry(ask_new_values,font=font)
		date_edit.pack()
		date_edit.insert(0,date)

		name_edit = Entry(ask_new_values,font=font)
		name_edit.pack()
		name_edit.insert(0,name)

		amount_edit = Entry(ask_new_values,font=font)
		amount_edit.pack()
		amount_edit.insert(0,amount)

		site_edit = Entry(ask_new_values,font=font)
		site_edit.pack()
		site_edit.insert(0,site)

		options = StringVar()
		category_edit = Entry(ask_new_values,font=font)
		category_edit.pack()
		category_edit.insert(0,category)

		payement_edit = ttk.Combobox(ask_new_values,textvariable=options)
		payement_edit['values'] = ("Credited","Debited","select")
		payement_edit.config(width=15)
		payement_edit.pack()
		payement_edit.current(payement)

		button_edit = Button(ask_new_values,text="Edit",command=lambda: edit_(num_))
		button_edit.pack()

	#add data
	column_s_no = 0
	total_amount = []

	for row in c.fetchall():
		column_s_no += 1
		data_table.insert(parent='',index='end',iid=row[0],text=row[0],values=(row[1],row[2],row[4],row[5],row[6],format_num(row[3])))
		total_amount.append(row[3])

	data_table.grid(row=2,column=0,sticky=N+S+W+E)
	
	label_total = Label(window_viewer,font=font,text=str("Total amount:" + format_num(str(sum(total_amount)))))
	label_total.grid(row=3,column=0,pady=20)

	status_viewer = LabelFrame(window_viewer,border=5)
	status_viewer.grid(row=4,column=0,columnspan=1)

	reset_button = Button(frame_button,width=22,image=img_reset,command=reset)
	reset_button.grid(row=0,column=0,pady=10)

	sort_data_button = Button(frame_button,image=img_sort,command=lambda: sort_data_and_destroy(file))
	sort_data_button.grid(row=0,column=1,sticky=W+E)

	change_file = Button(frame_button,image=img_choose_file,command=change_file_)
	change_file.grid(row=0,column=2,sticky=W+E)

	open_backup = Button(frame_button,image=img_choose_backup,command=backup_)
	open_backup.grid(row=0,column=3,sticky=W+E)

	delete_record = Button(frame_button,image=img_delete,command=selected_option_delete)
	delete_record.grid(row=0,column=4,sticky=W+E)

	edit_record = Button(frame_button,image=img_edit,command=selected_option_edit)
	edit_record.grid(row=0,column=5,sticky=W+E)

	export_record = Button(frame_button,image=img_export,command=export_window)
	export_record.grid(row=0,column=6,sticky=W+E)

	backup_record = Button(frame_button,image=img_backup,command=create_backup)
	backup_record.grid(row=0,column=7,sticky=W+E)

	send_record_ = Button(frame_button,image=img_mail,command=send_record)
	send_record_.grid(row=0,column=8,sticky=W+E)


	#to run the viewer's search from the main screen if input is provided
	if z == 1:
		search_api()



