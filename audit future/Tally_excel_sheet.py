import xlsxwriter
import sqlite3
import os
from styling import export_path
import threading
from tkinter import messagebox

def export_window():
    try:
        threading.Thread(target=convert_to_excel_sheet()).start()
        messagebox.showinfo("Export", "Export sucessful")
    except:
        messagebox.showerror("Export","Export unsucessful")

def convert_to_excel_sheet():
	
	workbook = xlsxwriter.Workbook(export_path)
	worksheet = workbook.add_worksheet()

	row = 0
	column = 0

	DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'appdata.db')
	conn = sqlite3.connect(DEFAULT_PATH)
	c = conn.cursor()
	c.execute('SELECT * FROM TALLY')

	element_list = ["Date","Name","Amount","Category","Payement","Site"]

	for elements in element_list:
		worksheet.write(row,column,elements)
		column += 1

	column = 0
	row = 1

	for item in c.fetchall():
		for i in range(6):
			if column != 2:
				worksheet.write(row,column,item[column])
			else:
				worksheet.write_number(row,column,item[2])
			column += 1
		if column == 6:
			row += 1
			column = 0
	workbook.close()
