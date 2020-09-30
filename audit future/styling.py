#version details
version = "0.0.1"







import os
from Tally_date import date
import json
from termcolor import colored
try:
	from pygame import mixer
	mixer.init()

	mixer.music.load('sucess.wav')
	mixer.music.set_volume(1)
	mixer.music.play()
	time.sleep(2)
	mixer.music.stop()
except:
	print(colored("Warning some of the future features of this app might not work with your device","yellow"))


#database
user_database = os.path.join(os.path.dirname(__file__),"userconfig.json")
help_path = ("file://"+os.path.join(os.path.dirname(__file__),"help.html"))
backup_path = os.path.join(os.path.dirname(__file__), "Backup")
backup_path_file = os.path.join(backup_path,date)
directory_database = os.path.dirname(__file__)
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'appdata.db')
DEFAULT_PATH1 = os.path.join(os.path.dirname(__file__), 'usersettings.db')

try:
	with open(user_database,"r") as read_file:
		data_retrieved = json.load(read_file)

	if str(data_retrieved["theme"]) != "dark theme":
		bg = "white"
		fg = "black"
		textbox_bg = "white"
		textbox_fg = "black"
		insert_fg = "black"
	else:
		bg = "black"
		fg = "white"
		textbox_bg = "gray20"
		textbox_fg = "white"
		insert_fg = "white"
except:
	bg = "white"
	fg = "black"
	textbox_bg = "white"
	textbox_fg = "black"
	insert_fg = "black"





#colour scheme

button_bg = "white"
button_fg = "black"
window_colour = "black"


#font
font = "courier"

status_down = False


#image sources 
image_reload = os.path.join(os.path.dirname(__file__),"Resources/unnamed.png")
image_back = os.path.join(os.path.dirname(__file__),"Resources/back.png")
image_icon_main_window = os.path.join(os.path.dirname(__file__),"Resources/auditfuture.ico")
image_back1 = os.path.join(os.path.dirname(__file__),"Resources/back1.png")

#button_width
b_wd = 13

#branding
company_name = ""
company_phone = ""
company_mail = ""

