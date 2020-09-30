from tkinter import *
from styling import *
from Tally_random_data import random_g
from tkinter import messagebox
import smtplib


def setting():

	settings_window = Tk()
	settings_window.title("Settings")
	settings_window.geometry("800x600")


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
			pass
		def _about_():
			pass
		def _feedback_():
			top = LabelFrame(panel_options,bg=bg)
			panel_options.add(top)

			label1 = Label(top, text="Type your name here:",fg=fg,bg=bg,font=font)
			label1.grid(row=1)

			gmail_adress_name = Entry(top, width=50)
			gmail_adress_name.config(fg=fg,bg=bg, insertbackground=fg)
			gmail_adress_name.grid(row=2)

			label2 = Label(top, text="Type your mail here:",fg=fg,bg=bg,font=font)
			label2.grid(row=3)

			gmail_adress_mail = Entry(top, width=50)
			gmail_adress_mail.config(fg=fg,bg=bg, insertbackground=fg)
			gmail_adress_mail.grid(row=4)

			label3 = Label(top, text="Type your feedback here:",fg=fg,bg=bg,font=font)
			label3.grid(row=5)

			gmail_adress_body = Text(top)
			gmail_adress_body.config(fg=fg,bg=bg, insertbackground=fg)
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
