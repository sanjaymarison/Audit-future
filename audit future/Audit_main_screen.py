#time module
import time
import datetime
start = time.time()

#gui module
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#system modules
import sys
import os
import threading
from termcolor import colored


#data processing and other data receiving modules
import sqlite3
from PIL import Image,ImageTk
from Audit_graph import graph_canvas
from Tally_people import advanced_data
import webbrowser
from Tally_excel_sheet import convert_to_excel_sheet
from Tally_viewer import viewer_api
import json
from Audit_upload import upload_to_cloud
#from Audit_android import start_android_beta

#own module for variables and other settings
from Tally_date import date
from styling import *
from Tally_backup import create_backup
from Tally_settings import setting
from user_config_window import check_user

'''
failed module need to be replace
None
'''
def window_start():
    check_user()
    print(colored("Audit future has started","green"))
    window_ = Tk()
    window_.title("Audit-Future" + "  " + str(version))
    window_.geometry("1350x700")
    window_.config(bg=window_colour)
    window_.iconbitmap(image_icon_main_window)
    


    def put_the_elements():
	    window = Canvas(window_,bg=bg,border=0,highlightthickness=1, highlightbackground=bg)
	    window.pack(fill=BOTH,expand=True)

	    with open(user_database,"r") as read_file:
	    	d = json.load(read_file)

	    def remove_text(element):
	    	element.delete(0,END)


	    frame_debit = LabelFrame(window,text="Debited/Credited",bg=bg,fg=fg,border=5,font=(font,16))
	    frame_debit.grid(row=3,column=0,columnspan=1,rowspan=10,pady=20,padx=100)

	    window_branding = Label(window,bg=bg,fg=fg,font=(font,30),text=company_name)
	    window_branding.grid(row=1,column=2,sticky=W,columnspan=1,pady=10) 

	    label_for_add_todays_details = Label(window,text="ADD TODAY'S REPORT",bg = bg , fg= fg)
	    label_for_add_todays_details.grid(row=2,column=1,columnspan=3,padx=10,pady=10)
	    label_for_add_todays_details.config(font=(font,20))

	    textbox_for_date = Entry(frame_debit,width=20)
	    textbox_for_date.grid(row=1,column=0,padx=10,pady=10)
	    textbox_for_date.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	    textbox_for_date.insert(0,"YYYY/MM/DD")
	    textbox_for_date.bind("<Button-1>",lambda x: remove_text(textbox_for_date))

	    text_box_for_name = Entry(frame_debit,width=20)
	    text_box_for_name.grid(row=2,column=0,padx=10,pady=10)
	    text_box_for_name.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	    text_box_for_name.insert(0,"Name")
	    text_box_for_name.bind("<Button-1>",lambda x: remove_text(text_box_for_name))

	    textbox_for_amount = Entry(frame_debit,width=20)
	    textbox_for_amount.grid(row=6,column=0,pady=10,padx=0)
	    textbox_for_amount.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	    textbox_for_amount.insert(0,"Amount")
	    textbox_for_amount.bind("<Button-1>",lambda x: remove_text(textbox_for_amount))

	    textbox_for_category = Entry(frame_debit,width=20)
	    textbox_for_category.grid(row=3,column=0,padx=20,pady=10)
	    textbox_for_category.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	    textbox_for_category.insert(1,"Category")
	    textbox_for_category.bind("<Button-1>",lambda x: remove_text(textbox_for_category))


	    clicked = StringVar()
	    chooose_option = ttk.Combobox(frame_debit,textvariable=clicked)
	    chooose_option['values'] = ("Credited","Debited","select")
	    chooose_option.config(width=15)
	    chooose_option.current(2)
	    chooose_option.grid(row=5,column=0,padx=10,pady=10)

	    if status_down == True:
	        status = Label(window,bd=1,height=30,relief=SUNKEN,bg=bg)
	        status.grid(row=24,column=0,columnspan=10,sticky=W+E,padx=20)

	        comapany_name_label = Label(status,bg=bg,fg=fg,font=(font,20),text=company_name)
	        comapany_name_label.grid(row=0,column=0,sticky=W+E)

	        comapany_phone_label = Label(status,bg=bg,fg=fg,font=(font,20),text=company_phone)
	        comapany_phone_label.grid(row=0,column=1,sticky=W+E)

	        comapany_mail_label = Label(status,bg=bg,fg=fg,font=(font,20),text=company_mail)
	        comapany_mail_label.grid(row=0,column=2,sticky=W+E)

	    textbox_for_site = Entry(frame_debit,width=20)
	    textbox_for_site.grid(row=4,column=0,padx=10,pady=10)
	    textbox_for_site.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	    textbox_for_site.insert(0,"Site No")
	    textbox_for_site.bind("<Button-1>",lambda x: remove_text(textbox_for_site))

	    top_status = Label(window,bd=1,bg=bg,fg=fg,font=font)
	    top_status.grid(row=0,column=0,sticky=W+E,columnspan=12)

	    #main window reload function
	    def reload_main_window():
	        window.destroy()
	        window_start()

	    img = Image.open(image_back)  # PIL solution
	    img = img.resize((50, 50), Image.ANTIALIAS) #The (250, 250) is (height, width)
	    img = ImageTk.PhotoImage(img) # convert to PhotoImage

	    
	    global i
	    i = 0

	    global x
	    x = 0

	    def insert_into_database():
	            i = 0
	            type_payement = str(clicked.get())
	            date_entered = str(textbox_for_date.get())
	            name_entered = str(text_box_for_name.get())
	            site_entered = str(textbox_for_site.get())
	            amount_entered = int(textbox_for_amount.get())
	            category_entered = textbox_for_category.get()

	            if date_entered == "YYYY/MM/DD":
	                    date_entered = date

	            if name_entered == "Name":
	                    label_for_error = Label(window,text="Please enter a valid name")
	                    label_for_error.grid(row=4,column=3,columnspan=4)
	                    label_for_error.config(bg=bg,fg=fg,font=font)
	                    i += 1

	            elif name_entered != "Name":
	                    label_for_error = Label(window,bg=bg,fg=fg,font=font,text="                                      ")
	                    label_for_error.grid(row=4,column=3,columnspan=4)
	                        
	                    i = 0

	            if type_payement == "select":
	                label_for_error = Label(window,text="Please select a valid type of payement")
	                label_for_error.grid(row=5,column=1,columnspan=4)
	                label_for_error.config(bg=bg,fg=fg,font=font)
	                i += 1
	            elif type_payement != "select":
	                label_for_error = Label(window,bg=bg,fg=fg,font=font,text="                                              ")
	                label_for_error.grid(row=5,column=1,columnspan=4)

	            
	    		
	    		
	    		
	            if i == 0:
	                time_ = datetime.datetime.now()
	                def insert_final_database():
	                    conn = sqlite3.connect(DEFAULT_PATH)
	                    c = conn.cursor()
	                    try:
	                        conn.execute('''CREATE TABLE IF NOT EXISTS TALLY(date TEXT,
	                                                                        name TEXT,
	                                                                        amount INT,
	                                                                        category TEXT,
	                                                                        payement TEXT,
	                                                                        site TEXT,
	                                                                        time TEXT)''')
	                    except Exception as e:
	                        print(e)

	                    c.execute('INSERT INTO TALLY (date , name , amount , category, payement, site,time) VALUES(?, ? ,? , ?, ?, ?, ?)',(date_entered,name_entered,amount_entered,category_entered,type_payement,site_entered,time_))
	                    conn.commit()
	                    c.close()
	                    conn.close()

	                insert_final_database()
	                    
	            
	    def quit():
	        def sure_quit():
	            sys.exit()



	        response1 = messagebox.askyesno("EXIT","Are you sure you want to quit?")
	        if response1 == 1:
	            sure_quit()

	        elif response1 == 0:
	            pass

	        
	       

	    def search_function():

	        database_search_window = LabelFrame(window,text="Search",bg=bg,fg=fg,border=5,font=(font,16))
	        database_search_window.grid(row=3,column=2,columnspan=1,rowspan=10,pady=20,padx=100)
	            
	        def search():

	            provided_date = str(textbox_search_date.get())
	            provided_name = str(textbox_search_name.get())
	            provided_amount = str(textbox_search_amount.get())
	            provided_category = str(textbox_search_category.get())
	            provided_payement = str(payement_search_result.get())
	            provided_site = str(textbox_for_site_search.get())

	            if provided_payement == "select":
	            	provided_payement = "Payement"

	            viewer_api(date1=provided_date,amount1=provided_amount,payement1=provided_payement,site1=provided_site,name1=provided_name,category1=provided_category)

	        textbox_search_date = Entry(database_search_window,width=20)
	        textbox_search_date.grid(row=0,column=0,padx=10,pady=10)
	        textbox_search_date.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	        textbox_search_date.insert(0,"Date")
	        textbox_search_date.bind("<Button-1>",lambda x: remove_text(textbox_search_date))

	        textbox_search_name = Entry(database_search_window,width=20)
	        textbox_search_name.grid(row=1,column=0,padx=10,pady=10)
	        textbox_search_name.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	        textbox_search_name.insert(0,"Name")
	        textbox_search_name.bind("<Button-1>",lambda x: remove_text(textbox_search_name))

	        textbox_search_amount = Entry(database_search_window,width=20)
	        textbox_search_amount.grid(row=5,column=0,pady=10,padx=0)
	        textbox_search_amount.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	        textbox_search_amount.insert(0,"Amount")
	        textbox_search_amount.bind("<Button-1>",lambda x: remove_text(textbox_search_amount))

	        textbox_search_category = Entry(database_search_window,width=20)
	        textbox_search_category.grid(row=2,column=0,padx=20,pady=10)
	        textbox_search_category.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	        textbox_search_category.insert(0,"Category")
	        textbox_search_category.bind("<Button-1>",lambda x: remove_text(textbox_search_category))

	        payement_search_result = StringVar()
	        payement_search_result.set("select")

	        textbox_for_site_search = Entry(database_search_window,width=20)
	        textbox_for_site_search.grid(row=3,column=0,padx=10,pady=10)
	        textbox_for_site_search.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	        textbox_for_site_search.insert(0,"Site")
	        textbox_for_site_search.bind("<Button-1>",lambda x: remove_text(textbox_for_site_search))
	        
	        payement_search = ttk.Combobox(database_search_window,textvariable=payement_search_result)
	        payement_search['values'] = ("Credited","Debited","select")
	        payement_search.current(2)
	        payement_search.grid(row=4,column=0)
	        payement_search.config(width=15)


	        button_search = Button(database_search_window,bg=button_bg,fg=button_fg,font=font,text="Search",command=search)
	        button_search.grid(row=6,column=0,pady=10)

	    	


	    def view():
	    	viewer_api()




	    button_to_put_todays_details = Button(frame_debit,text="ADD",bg=button_bg,fg=button_fg,command=insert_into_database)
	    button_to_put_todays_details.grid(row=7,column=0,pady=10)
	    button_to_put_todays_details.config(font=font)

	    label_for_date = Label(window,text=date,bg=bg,fg=fg,font=(font,30))
	    label_for_date.grid(row=2,column=0,columnspan=1)
	    label_for_date.config(font=font)


	    def delete():
	        database_delete_window = LabelFrame(window,text="DELETE",bg=bg,fg=fg,border=5,font=(font,16))
	        database_delete_window.grid(row=3,column=4,columnspan=1,rowspan=10,pady=20,padx=100)
	        
	        textbox_get_date = Entry(database_delete_window,width=20)
	        textbox_get_date.grid(row=0,column=0,padx=10,pady=10)
	        textbox_get_date.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	        textbox_get_date.insert(0,"YYYY/MM/DD")
	        textbox_get_date.bind("<Button-1>",lambda x: remove_text(textbox_get_date))

	        text_box_get_name = Entry(database_delete_window,width=20)
	        text_box_get_name.grid(row=1,column=0,padx=10,pady=10)
	        text_box_get_name.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	        text_box_get_name.insert(0,"Name")
	        text_box_get_name.bind("<Button-1>",lambda x: remove_text(text_box_get_name))

	        textbox_get_amount = Entry(database_delete_window,width=20)
	        textbox_get_amount.grid(row=5,column=0,pady=10,padx=0)
	        textbox_get_amount.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	        textbox_get_amount.insert(0,"₹")
	        textbox_get_amount.bind("<Button-1>",lambda x: remove_text(textbox_get_amount))

	        textbox_get_category = Entry(database_delete_window,width=20)
	        textbox_get_category.grid(row=2,column=0,padx=20,pady=10)
	        textbox_get_category.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	        textbox_get_category.insert(1,"Category")
	        textbox_get_category.bind("<Button-1>",lambda x: remove_text(textbox_get_category))

	        clicked_get = StringVar()
	        chooose_get_option = ttk.Combobox(database_delete_window,textvariable=clicked_get)
	        chooose_get_option['values'] = ("Credited","Debited","select")
	        chooose_get_option.config(width=15)
	        chooose_get_option.current(2)
	        chooose_get_option.grid(row=4,column=0,padx=10,pady=10)

	        textbox_for_site_delete = Entry(database_delete_window,width=20)
	        textbox_for_site_delete.grid(row=3,column=0,padx=10,pady=10)
	        textbox_for_site_delete.config(bg=textbox_bg,fg=textbox_fg,insertbackground=insert_fg)
	        textbox_for_site_delete.insert(0,"Site No")
	        textbox_for_site_delete.bind("<Button-1>",lambda x: remove_text(textbox_for_site_delete))

	        def delete_final():

	            date_to_delete = str(textbox_get_date.get())
	            name_to_delete = str(text_box_get_name.get())
	            amount_to_delete = int(textbox_get_amount.get())
	            category_to_delete = str(textbox_get_category.get())
	            clicked_to_delete = str(clicked_get.get())
	            textbox_of_site_delete = str(textbox_for_site_delete.get())

	            conn = sqlite3.connect(DEFAULT_PATH)
	            c = conn.cursor()
	            c.execute('DELETE FROM TALLY WHERE date=? AND name=? AND amount=? AND category=? AND payement=? AND site=?',(date_to_delete,name_to_delete,amount_to_delete,category_to_delete,clicked_to_delete,textbox_of_site_delete))
	            conn.commit()
	            conn.close()

	        delete_button_final = Button(database_delete_window,text="Delete",bg=button_bg,fg=button_fg,font=font,command=delete_final)
	        delete_button_final.grid(row=6,column=0)




	    def grapher():
	        graph_window = Toplevel()
	        graph_window.config(bg=bg)
	        graph_window.geometry("200x200")

	        def credited():

	            threading.Thread(target=graph("Credited")).start()

	        def debited():

	            threading.Thread(target=graph("Debited")).start()

	        def total():

	            threading.Thread(target=total_graph()).start()

	        button_debited = Button(graph_window,bg=button_bg,fg=button_fg,font=font,text="Debited",command=debited)
	        button_debited.grid(row=0,column=0,padx=10,pady=10)

	        button_credited = Button(graph_window,bg=button_bg,fg=button_fg,font=font,text="Credited",command=credited)
	        button_credited.grid(row=0,column=1,padx=10,pady=1)

	        button_total = Button(graph_window,bg=button_bg,fg=button_fg,font=font,text="Total",command=total_graph)
	        button_total.grid(row=1,column=0,padx=10,pady=1)



	    def calculator():
	        try:
	            os.system("open -a calculator")
	        except:
	            os.system("calc")


	    def help_open():
	        try:
	            webbrowser.open(help_path)
	        except:
	            messagebox.showerror("Error","Couldn't find a browser/file")

	    def export_window():
	        try:
	            threading.Thread(target=convert_to_excel_sheet()).start()
	            messagebox.showinfo("Export", "Export sucessful")
	        except:
	            messagebox.showerror("Export","Export unsucessful")

	    calculator_button = Button(top_status,text="Calculator",command=calculator,width=b_wd)
	    calculator_button.grid(row=0,column=7)
	    calculator_button.config(bg=button_bg,fg=button_fg,font=font)

	    #fullscreen = Button(top_status,bg=button_bg,fg=button_fg,font=font,text="FULL SCREEN",width=b_wd,command=fullscreen)
	    #fullscreen.grid(row=0,column=4,pady=10)

	    #theme_button = Button(window,bg=fg,fg=bg,text="Theme",font=font)
	    #theme_button.grid(row=1,column=6,sticky=W+E,pady=10)


	    upload_button = Button(top_status,bg=button_bg,fg=button_fg,width=b_wd,font=font,text="Upload",command=upload_to_cloud)
	    upload_button.grid(row=0,column=3)

	    help_button = Button(top_status,bg=button_bg,width=b_wd,fg=button_fg,font=font,text="HELP",command=help_open)
	    help_button.grid(row=0,column=8)

	    backup_button = Button(top_status,bg=button_bg,width=b_wd,fg=button_fg,font=font,text="Backup",command=create_backup)
	    backup_button.grid(row=0,column=2)

	    export_button = Button(top_status,bg=button_bg,width=b_wd,fg=button_fg,font=font,text="Export",command=export_window)
	    export_button.grid(row=0,column=1)

	    full_database = Button(top_status,width=b_wd,text="View",bg=button_bg,fg=button_fg,font=font,command=view)
	    full_database.grid(row=0,column=0)

	    quit_button = Button(top_status,width=b_wd,text="Exit",bg=button_bg,fg=button_fg,font=font,command=quit)
	    quit_button.grid(row=0,column=10)

	    graph_button = Button(top_status,width=b_wd,text="GRAPH",command=lambda: graph_canvas(window=window_,window1=put_the_elements,window2=window))
	    graph_button.grid(row=0,column=4,pady=10)
	    graph_button.config(bg=button_bg,fg=button_fg,font=font)

	    def adv_dat():
	    	window.destroy()
	    	advanced_data(window=window_,window1=put_the_elements)


	    advanced_data_button = Button(top_status,width=10,text="Other Data",command=adv_dat)
	    advanced_data_button.grid(row=0,column=6,pady=10)
	    advanced_data_button.config(bg=button_bg,fg=button_fg,font=font)


	    settings_ = Button(top_status,width=10,text="Settings",bg=button_bg,fg=button_fg,font=font,command=setting)
	    settings_.grid(row=0,column=9,pady=10)

	    delete()
	    search_function()
	    global end
	    end = time.time()
	    print(colored("Audit future rendering completed","green"))
	    print("["+colored("login","green")+"]","user has been logged in")
	    time__ = str(datetime.datetime.now())
	    print("["+colored("logged in at","green")+"]",colored(time__,"yellow"))
	    print("["+colored("user name","green")+"]",d["name"])
	    print(colored("first time user:","yellow"),colored(d["first_time"],"green"))
	    print("["+colored("user theme","green")+"]",d["theme"])

	    window.mainloop()

    put_the_elements()
    
window_start()
print(colored("App status of last boot:","green"))
print("Time taken to start: "+colored(str(end-start),"yellow")+" Seconds")

