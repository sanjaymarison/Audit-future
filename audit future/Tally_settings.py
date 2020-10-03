from tkinter import *
from styling import *
from Tally_random_data import random_g
from tkinter import messagebox,filedialog
import smtplib
import webbrowser
import json
import styling
import os

def setting():

	settings_window = Tk()
	settings_window.title("Settings")
	settings_window.geometry("800x650")
	messagebox.showinfo("Note","You have to restart the app for the changes you make here to update")


	class information:
		def _folder_():
			pass
		def _display_():
			pass
		def _file_():
			pass
		def _branding_():
			pass
		def _export_():
			def choose_location():
				settings_window.file_choose = filedialog.askdirectory()
				text_path.delete(0,"end")
				text_path.insert(0,settings_window.file_choose)
			def exit_export():
				window_export.destroy()
			def save_path_():
				path_ = str(text_path.get())
				with open(user_database,"r") as read_file:
					d = json.load(read_file)
				d["export-path"] = path_
				print(d)
				with open(user_database,"w") as write_file:
					json.dump(d,write_file)
				notify_saved = Label(window_export,bg=bg,fg=fg,text="Saved",font=font)
				notify_saved.grid(row=3,column=0)

			window_export = LabelFrame(panel_options,bg=bg)
			panel_options.add(window_export)

			path_heading = Label(window_export,bg=bg,fg=fg,text="Enter path to export excel file:",font=font)
			path_heading.grid(row=0,column=0)

			text_path = Entry(window_export,bg=textbox_bg,fg=textbox_fg,width=30,insertbackground=insert_fg,font=font)
			text_path.grid(row=1,column=0)
			text_path.insert(0,export_path)

			save_path = Button(window_export,bg=button_bg,fg=button_fg,text="Save",command=save_path_)
			save_path.grid(row=2,column=0)

			file_dialog_box = Button(window_export,bg=button_bg,fg=button_fg,font=font,text="Choose location",command=choose_location)
			file_dialog_box.grid(row=2,column=1)

			exit_button = Button(window_export,fg=button_fg,bg=button_bg,font=font,text="Exit",command=exit_export)
			exit_button.grid(row=3,column=1)			


		def _about_():
			def open_t_c():
				try:
					webbrowser.open(tc_path)
				except:
					messagebox.showerror("Error","Couldn't find a browser/file")
			def exit_about():
				window_about.destroy()
			about_text = "This app is a product of future lab, run and manged by sanjay marison. Any kind of changes done to this app must be in accordance with the license agreement. Some of the features might not be working and will be fixed in the future updates. Any feedback can be given by choosing the option on the left menu. Note many features are experimental and might not make to the stable release of the app, any of those changes will be notified in the about menu of the app. version : 0.0.1 beta for developers author : Sanjay Marison mail : marisonsanjay@gmail.com"
			window_about = LabelFrame(panel_options,bg=bg)
			panel_options.add(window_about)

			about_heading = Label(window_about,bg=bg,fg=fg,text="About",font=(font,30))
			about_heading.grid(row=0,column=0)

			about_info = Message(window_about,bg=bg,fg=fg,font=(font,24),text=about_text)
			about_info.grid(row=1,column=0,columnspan=2)

			button_terms = Button(window_about,bg=button_bg,fg=button_fg,text="Terms and conditions",command=open_t_c)
			button_terms.grid(row=2,column=0)

			exit_button = Button(window_about,fg=button_fg,bg=button_bg,font=font,text="Exit",command=exit_about)
			exit_button.grid(row=2,column=1)

		def _feedback_():
			top = LabelFrame(panel_options,bg=bg)
			panel_options.add(top)

			label1 = Label(top, text="Type your name here:",fg=fg,bg=bg,font=font)
			label1.grid(row=1)

			gmail_adress_name = Entry(top, width=50)
			gmail_adress_name.config(fg=textbox_fg,bg=textbox_bg, insertbackground=insert_fg)
			gmail_adress_name.grid(row=2)

			label2 = Label(top, text="Type your mail here:",fg=fg,bg=bg,font=font)
			label2.grid(row=3)

			gmail_adress_mail = Entry(top, width=50)
			gmail_adress_mail.config(fg=textbox_fg,bg=textbox_bg, insertbackground=insert_fg)
			gmail_adress_mail.grid(row=4)

			label3 = Label(top, text="Type your feedback here:",fg=fg,bg=bg,font=font)
			label3.grid(row=5)

			gmail_adress_body = Text(top)
			gmail_adress_body.config(fg=textbox_fg,bg=textbox_bg, insertbackground=insert_fg)
			gmail_adress_body.grid(row=6)

			def exit_feedback():
				top.destroy()

			exit_button = Button(top,fg=button_fg,bg=button_bg,font=font,text="Exit",command=exit_feedback)
			exit_button.grid(row=8,pady=10)



			def sendit():
				complete_body ="name:    " +  gmail_adress_name.get() + "\nmail:   " + gmail_adress_mail.get() + "\n\nfeedback:    " + str(gmail_adress_body.get("1.0","end-1c"))
				EMAIL_ADRESS = "pythonprojectmail1@gmail.com"

				EMAIL_PASSWORD = "vrzdoskkghtvhyjv"
				SENDERSMAILID = "sanjaymarison@gmail.com"

				with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
				    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)

				    subject = "feedback from tally app"
				    body = complete_body

				    msg = f'subject:{subject}\n\n{body}'

				    smtp.sendmail(EMAIL_ADRESS, SENDERSMAILID, msg)

				    label4 = Label(top, text="YOUR FEEDBACK HAS BEEN SENT",fg=fg,bg=bg)
				    label4.grid(row=7)


			send_button = Button(top,fg=button_fg,bg=button_bg,font=font,text="Submit",command=sendit)
			send_button.grid(row=7)



		def _developer_():
						
			window_dev = LabelFrame(panel_options,bg=bg)
			panel_options.add(window_dev)

			def random_data():
				random_g(user_input=int(text_data_size.get()))
				messagebox.showinfo("Sucess","Insert sucessful")


			fake_data = Label(window_dev,text="FAKE DATA",bg=bg,fg=fg,font=(font,30))
			fake_data.grid(row=0,column=0)

			text_data_size = Entry(window_dev,insertbackground=fg,fg=fg,bg=bg,font=font)
			text_data_size.grid(row=1,column=0,pady=20)

			button_go = Button(window_dev,text="Generate and insert",bg=button_bg,fg=button_fg,font=font,command=random_data)
			button_go.grid(row=2,column=0,pady=20)

			def exit_developer():
				window_dev.destroy()

			exit_button = Button(window_dev,fg=button_fg,bg=button_bg,font=font,text="Exit",command=exit_developer)
			exit_button.grid(row=3,column=0,pady=10)

			window_dev.mainloop()



	#panel for button
	panel_options = PanedWindow(settings_window,bd=20,relief="raised",bg=bg)
	panel_options.pack(fill=BOTH,expand=1)

	#frame for button
	frame_options = LabelFrame(panel_options,bg=bg)
	panel_options.add(frame_options)

	#button 
	button_store = Button(frame_options,bg=button_bg,fg=button_fg,font=font,text="Folder",height=5,command=information._folder_)
	button_store.grid(row=0,column=0,sticky=W+E)

	button_display = Button(frame_options,bg=button_bg,fg=button_fg,font=font,text="Display",height=5,command=information._display_)
	button_display.grid(row=1,column=0,sticky=W+E)

	button_backup = Button(frame_options,bg=button_bg,fg=button_fg,font=font,text="Backup",height=5,command=information._file_)
	button_backup.grid(row=2,column=0,sticky=W+E)

	button_branding = Button(frame_options,bg=button_bg,fg=button_fg,font=font,text="Branding",height=5,command=information._branding_)
	button_branding.grid(row=3,column=0,sticky=W+E)

	button_export = Button(frame_options,bg=button_bg,fg=button_fg,font=font,text="Export",height=5,command=information._export_)
	button_export.grid(row=4,column=0,sticky=W+E)

	button_feedback = Button(frame_options,bg=button_bg,fg=button_fg,font=font,text="Feedback",height=5,command=information._feedback_)
	button_feedback.grid(row=5,column=0,sticky=W+E)

	button_developer = Button(frame_options,bg=button_bg,fg=button_fg,font=font,text="Developer",height=5,command=information._developer_)
	button_developer.grid(row=6,column=0,sticky=W+E)

	button_about = Button(frame_options,bg=button_bg,fg=button_fg,font=font,text="About",height=5,command=information._about_)
	button_about.grid(row=7,column=0,sticky=W+E)

	panel_information = PanedWindow(settings_window,bg=bg,bd=4,relief="raised",orient=HORIZONTAL)
	panel_options.add(panel_information)

	frame_information = LabelFrame(panel_information,bg=fg)
	panel_information.add(frame_information)

	settings_window.mainloop()
