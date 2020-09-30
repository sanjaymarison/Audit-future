import json
import sys
from styling import *
from tkinter import *
from tkinter import messagebox
import datetime



def first_time_user_config_window():
	time = str(datetime.datetime.now())

	def get_details(r,v,t,z):
		name = str(name_of_user.get())
		mail = str(mail_of_user.get())
		country = str(country_of_user.get())
		state = str(state_of_user.get())
		city = str(city_of_user.get())
		pin = str(pin_of_user.get())
		contact = str(contact_of_user.get())
		company = str(company_of_user.get())
		r = int(r.get())
		v = int(v.get())
		t = int(t.get())
		z = int(z.get())

		check = [name,mail,country,state,city,pin,contact,company]
		print("user data")
		print(check)
		for elements in check:
			if elements == "":
				print(elements)
				messagebox.showerror("Error","Fill out all fields before submitting")

		if r == 1:
			r = "light theme"
		elif r == 2:
			r = "dark theme"

		if t == 1:
			t = "branding"
		elif t == 2:
			t = "no branding"
		if v == 1:
			v = "send"
		elif v ==2:
			v = "dont send"
		if z == 1:
			z = "agree"
			data = {
				"first_time":"False",
				"name": name,
				"mail": mail,
				"country": country,
				"state": state,
				"city": city,
				"pin": pin,
				"contact": contact,
				"company": company,
				"theme": r,
				"branding": t,
				"usage": v,
				"registered-on": time
			}
			with open(user_database,"w") as write_file:
				json.dump(data,write_file)

			messagebox.showinfo("Relaunch","Relaunch app to continue")
			sys.exit()
		elif z == 2:
			z = "disagree"
			messagebox.showerror("Terms & Conditions","Please accept the Terms and Conditions to continue")

	user_window = Tk()
	user_window.config(bg=bg)
	user_window.title("Welcome to audit-future")
	welcome = Label(user_window,bg=bg,fg=fg,font=(font,40),text="Welcome To Audit Future")
	welcome.grid(row=0,column=1,pady=10,padx=100)

	frame_ = LabelFrame(user_window,bg=bg)
	frame_.grid(row=1,column=0,columnspan=2)

	label_name = Label(frame_,bg=bg,fg=fg,font=font,text="Name:")
	label_name.grid(row=0,column=0,sticky=W,padx=40)

	name_of_user = Entry(frame_,fg=textbox_fg,bg=textbox_bg,insertbackground=insert_fg,width=30,font=font)
	name_of_user.grid(row=1,column=0,padx=40)

	label_mail = Label(frame_,bg=bg,fg=fg,font=font,text="Mail:")
	label_mail.grid(row=0,column=1,sticky=W,padx=40)

	mail_of_user = Entry(frame_,fg=textbox_fg,bg=textbox_bg,insertbackground=insert_fg,width=30,font=font)
	mail_of_user.grid(row=1,column=1,padx=40)

	label_country = Label(frame_,bg=bg,fg=fg,font=font,text="Country:")
	label_country.grid(row=2,column=1,sticky=W,padx=40)

	country_of_user = Entry(frame_,fg=textbox_fg,bg=textbox_bg,insertbackground=insert_fg,width=30,font=font)
	country_of_user.grid(row=3,column=1,padx=40)

	label_state = Label(frame_,bg=bg,fg=fg,font=font,text="State:")
	label_state.grid(row=4,column=0,sticky=W,padx=40)

	state_of_user = Entry(frame_,fg=textbox_fg,bg=textbox_bg,insertbackground=insert_fg,width=30,font=font)
	state_of_user.grid(row=5,column=0,padx=40)

	label_city = Label(frame_,bg=bg,fg=fg,font=font,text="City:")
	label_city.grid(row=6,column=0,sticky=W,padx=40)

	city_of_user = Entry(frame_,fg=textbox_fg,bg=textbox_bg,insertbackground=insert_fg,width=30,font=font)
	city_of_user.grid(row=7,column=0,padx=40)

	label_pin = Label(frame_,bg=bg,fg=fg,font=font,text="Pin Code:")
	label_pin.grid(row=6,column=1,sticky=W,padx=40)

	pin_of_user = Entry(frame_,fg=textbox_fg,bg=textbox_bg,insertbackground=insert_fg,width=30,font=font)
	pin_of_user.grid(row=7,column=1,padx=40)

	label_contact = Label(frame_,bg=bg,fg=fg,font=font,text="Contact Number:")
	label_contact.grid(row=4,column=1,sticky=W,padx=40)

	contact_of_user = Entry(frame_,fg=textbox_fg,bg=textbox_bg,insertbackground=insert_fg,width=30,font=font)
	contact_of_user.grid(row=5,column=1,padx=40)

	label_company = Label(frame_,bg=bg,fg=fg,font=font,text="Company Name:")
	label_company.grid(row=2,column=0,sticky=W,padx=40)

	company_of_user = Entry(frame_,fg=textbox_fg,bg=textbox_bg,insertbackground=insert_fg,width=30,font=font)
	company_of_user.grid(row=3,column=0,padx=40)

	label_theme = Label(frame_,bg=bg,fg=fg,font=font,text="Theme:")
	label_theme.grid(row=8,column=0,sticky=W,padx=40,pady=10)

	r = IntVar()
	r.set("2")
	Radiobutton(frame_,text="Light Theme",variable=r,value=1,bg=bg,fg=fg).grid(row=9,column=0)
	Radiobutton(frame_,text="Dark Theme",variable=r,value=2,bg=bg,fg=fg).grid(row=9,column=1)

	label_branding = Label(frame_,bg=bg,fg=fg,font=font,text="Show Branding in app:")
	label_branding.grid(row=10,column=0,sticky=W,padx=40,pady=10)

	t = IntVar()
	t.set("2")
	Radiobutton(frame_,text="Yes",variable=t,value=1,bg=bg,fg=fg).grid(row=11,column=0)
	Radiobutton(frame_,text="No",variable=t,value=2,bg=bg,fg=fg).grid(row=11,column=1)


	label_usage = Label(frame_,bg=bg,fg=fg,font=font,text="Send Usage Report Statistics:")
	label_usage.grid(row=12,column=0,sticky=W,padx=40,pady=10)

	v = IntVar()
	v.set("1")
	Radiobutton(frame_,text="Send",variable=v,value=1,bg=bg,fg=fg).grid(row=13,column=0,pady=0)
	Radiobutton(frame_,text="Don't Send",variable=v,value=2,bg=bg,fg=fg).grid(row=13,column=1,pady=0)

	label_tc = Label(frame_,bg=bg,fg=fg,font=font,text="Terms and Conditions")
	label_tc.grid(row=14,column=0,sticky=W,padx=40,pady=12)

	z = IntVar()
	z.set("2")
	Radiobutton(frame_,text="Agree",variable=z,value=1,bg=bg,fg=fg).grid(row=15,column=0,pady=0)
	Radiobutton(frame_,text="Disagree",variable=z,value=2,bg=bg,fg=fg).grid(row=15,column=1,pady=0)

	submit_user_input = Button(user_window,text="Submit",bg=button_bg,fg=button_fg,font=font,command=lambda: get_details(r=r,v=v,t=t,z=z))
	submit_user_input.grid(row=2,column=1,pady=20)


	user_window.mainloop()


def check_user():
	with open(user_database,"r") as read_file:
		d = json.load(read_file)
	if d["first_time"] == "True":
		first_time_user_config_window()
		sys.exit()
	else:
		pass


