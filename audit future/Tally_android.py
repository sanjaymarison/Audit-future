import kivy
import os
import time
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3

class front_page(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		z = 0
		try:
			DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'appdata.db')
			conn = sqlite3.connect(DEFAULT_PATH)
			c = conn.cursor()
			c.execute("SELECT * FROM TALLY")

			elements = ["Sort No","Date","Name","Amount","Category","Payement","Site No"]

			for element in elements:
				self.add_widget(Label(text=str(element)))

			self.cols = 7

			for row in c.fetchall():
				
				z+=1
				self.add_widget(Label(text=str(z)))
				for x in range(6):
					self.add_widget(Label(text=str(row[x])))
		except:
			self.cols = 1
			self.add_widget(Label(text="Nothing to show here"))
			self.add_widget(Label(text="add something in your main app and upload to show here"))
			self.add_widget(Label(text="If you have added data and uploaded but if it is not shown here,\n restart your app and check your internet connection"))
		self.go_back = Button(text="back")
		self.go_back.bind(on_press=self.takeback)
		bottom_line = GridLayout(cols=1)
		bottom_line.add_widget(self.go_back)
		self.add_widget(bottom_line)

	def takeback(self,instance):
		tally_app.screen_manager.current = "loading"


class load_page(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols = 1
		self.add_widget(Label(text="Welcome To Tally Viewer"))
		self.take_me_in = Button(text="Show",size_hint=(.25,.25),pos=(10,10))
		self.take_me_in.bind(on_press=self.go_in)
		self.add_widget(self.take_me_in)
		
	def go_in(self,instance):
		tally_app.screen_manager.current = "show_data"


class tally_viewer(App):
	def build(self):
		self.screen_manager = ScreenManager()

		self.loadpage = load_page()
		screen = Screen(name="loading")
		screen.add_widget(self.loadpage)
		self.screen_manager.add_widget(screen)

		self.frontpage = front_page()
		screen = Screen(name="show_data")
		screen.add_widget(self.frontpage)
		self.screen_manager.add_widget(screen)

		return self.screen_manager


if __name__ == "__main__":
	tally_app = tally_viewer()
	tally_app.run()
