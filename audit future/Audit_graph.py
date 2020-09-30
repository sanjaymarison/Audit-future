from tkinter import *
from styling import *
import time
import tkinter.ttk as ttk
from graphing import graph,total_graph
from PIL import Image,ImageTk
import threading
from termcolor import colored


def graph_canvas(window,window1,window2):
	print(colored("Graph canvas Started...","green"))
	window2.destroy()
	window5 = Canvas(window,bg=bg,border=0,highlightthickness=1, highlightbackground=bg)
	window5.pack(fill=BOTH,expand=True)

	def loading():
		label1.config(text="Loading")
		pb = ttk.Progressbar(status_of_graph, length=300, mode='indeterminate')
		pb.pack()
		pb.start(25)
		return pb

	def loaded(get_):
		label1.config(text="Loaded")
		get_.destroy()

	def credited():
		print(colored("Starting credited graph","yellow"))
		loading()
		graph("Credited")
		loaded(pb)

	def debited():
		print(colored("Starting debited graph","yellow"))
		loading()
		graph("Debited")
		loaded(pb)

	def total():
		loading()
		total_graph()
		loaded(pb)

	def main_screen():
		window5.destroy()
		window1()

	img1 = Image.open(image_back1)  # PIL solution
	img1 = img1.resize((50, 50), Image.ANTIALIAS) #The (250, 250) is (height, width)
	img1 = ImageTk.PhotoImage(img1) # convert to PhotoImage



	back_button = Button(window5,height=30,image=img1,bg=button_bg,command=main_screen)
	back_button.grid(row=0,column=0)

	graph_label = Label(window5,text="GRAPH",bg=bg,fg=fg,font=(font,40))
	graph_label.grid(row=0,column=1)

	frame_debit_graph = Button(window5,text="Debited",bg=button_bg,fg=button_fg,font=(font,16),height=20,width=10,command=debited)
	frame_debit_graph.grid(row=1,column=0,columnspan=1,pady=100,padx=100)

	frame_credit_graph = Button(window5,text="Credited",bg=button_bg,fg=button_fg,font=(font,16),height=20,width=10,command=credited)
	frame_credit_graph.grid(row=1,column=1,columnspan=1,pady=100,padx=100)

	frame_total_graph = Button(window5,text="Overall data",bg=button_bg,fg=button_fg,font=(font,16),height=20,width=10,command=total)
	frame_total_graph.grid(row=1,column=2,columnspan=1,pady=100,padx=100)

	status_of_graph = LabelFrame(window5,text="Graph status",bg=bg,fg=fg,border=5,font=(font,16))
	status_of_graph.grid(row=1,column=3,columnspan=1,pady=100,padx=20)

	label1 = Label(status_of_graph,text="Choose an option to continue",bg=bg,fg=fg,font=(font,16))
	label1.pack()

	print(colored("Graph canvas rendering completed","green"))
