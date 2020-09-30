from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.uix.label import Label
import os
import sqlite3

def start_android_beta():
	DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'appdata.db')
	conn = sqlite3.connect(DEFAULT_PATH)
	c = conn.cursor()
	c.execute("SELECT * FROM TALLY")

	elements = ["Sort No","Date","Name","Amount","Category","Payement","Site No"]

	layout = GridLayout(cols=7, spacing=10, size_hint_y=None)
	# Make sure the height is such that there is something to scroll.
	layout.bind(minimum_height=layout.setter('height'))
	for element in elements:
	    btn = Label(text=str(element), size_hint_y=None, height=40)
	    layout.add_widget(btn)

	x = 1
	for row in c.fetchall():
		but1 = Label(text=str(x), size_hint_y=None, height=40)
		but2 = Label(text=str(row[0]), size_hint_y=None, height=40)
		but3 = Label(text=str(row[1]), size_hint_y=None, height=40)
		but4 = Label(text=str(row[2]), size_hint_y=None, height=40)
		but5 = Label(text=str(row[3]), size_hint_y=None, height=40)
		but6 = Label(text=str(row[4]), size_hint_y=None, height=40)
		but7 = Label(text=str(row[5]), size_hint_y=None, height=40)
		x+=1
		v = [but1,but2,but3,but4,but5,but6,but7]
		for ele in v:
			layout.add_widget(ele)

	root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
	root.add_widget(layout)

	runTouchApp(root)