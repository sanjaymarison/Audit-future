import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from styling import DEFAULT_PATH,font,button_bg,button_fg,user_name
from tkinter import Toplevel,Entry,Button

def send_record():
	sender = Toplevel()
	sender.resizable(False,False)
	who = Entry(sender,bg="white",fg="black",insertbackground="black",font=font)
	who.pack()
	who.insert(0,"Sender:")
	def remove_():
		who.delete(0,'end')
	who.bind("<Button-1>",lambda x:remove_())

	def send():
		mail_content = f'''
		Audit future Record

		Current active database

		sent by user{user_name}

		'''
		#The mail addresses and password
		sender_address = 'pythonprojectmail1@gmail.com'
		sender_pass = 'vrzdoskkghtvhyjv'
		receiver_address = (who.get())
		#Setup the MIME
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = 'Audit future Record'
		#The subject line
		#The body and the attachments for the mail
		message.attach(MIMEText(mail_content, 'plain'))
		attach_file_name = DEFAULT_PATH
		attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
		payload = MIMEBase('application', 'octate-stream')
		payload.set_payload((attach_file).read())
		encoders.encode_base64(payload) #encode the attachment
		#add payload header with filename
		payload.add_header('Content-Decomposition', 'attachment', filename="appdata.db")
		message.attach(payload)
		#Create SMTP session for sending the mail
		session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
		session.starttls() #enable security
		session.login(sender_address, sender_pass) #login with mail_id and password
		text = message.as_string()
		session.sendmail(sender_address, receiver_address, text)
		session.quit()
		sender.destroy()
		print("Mail sent to user")

	button_send = Button(sender,bg=button_bg,fg=button_fg,font=font,text="Send",command=send)
	button_send.pack()