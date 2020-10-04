#version details
version = "0.0.2"

import os
from Tally_date import date
import json
from termcolor import colored
try:
	from pygame import mixer
	error_sound = mixer.music.load('error.wav')
	sucess_sound = mixer.music.load('sucess.wav')
except:
	print(colored("Warning some of the future features of this app might not work with your device","yellow"))


#database
user_database = os.path.join(os.path.dirname(__file__),"userconfig.json")
help_path = ("file://"+os.path.join(os.path.dirname(__file__),"help.html"))
tc_path = ("file://"+os.path.join(os.path.dirname(__file__),"terms_and_conditions.html"))
backup_path = os.path.join(os.path.dirname(__file__), "Backup")
backup_path_file = os.path.join(backup_path,date)
directory_database = os.path.dirname(__file__)
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'appdata.db')
DEFAULT_PATH1 = os.path.join(os.path.dirname(__file__), 'usersettings.db')
export_path = str(os.path.join(os.path.dirname(__file__),"audit_export.xlsx"))
app_path = str(os.path.join(os.path.dirname(__file__),"Audit_main_screen.py"))

with open(user_database,"r") as read_file:
		data_retrieved = json.load(read_file)

def reconfig_path():
	try:
		export_path1 = str(data_retrieved["export-path"])
		export_path1 = os.path.join(export_path1,"audit_export.xlsx")
		print(export_path1)
		return export_path1
		
	except:
		print("App opened first time so leaving reconfig_path")

export_path1 = reconfig_path()

if str(export_path1) == "None/audit_export.xlsx":
	pass
else:
	export_path = export_path1


try:
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

try:
	if str(data_retrieved["branding"]) == "branding":
		status_down = True
	else:
		status_down = False
except:
	print("App opened first time so leaving branding")

#image sources 
image_reload = os.path.join(os.path.dirname(__file__),"Resources/unnamed.png")
image_back = os.path.join(os.path.dirname(__file__),"Resources/back.png")
image_search = os.path.join(os.path.dirname(__file__),"Resources/search.png")
image_icon_main_window = os.path.join(os.path.dirname(__file__),"Resources/auditfuture.ico")

#button_width
b_wd = 13

#branding
try:
	user_name = str(data_retrieved["name"])
	company_name = str(data_retrieved["company"]).upper()
	company_phone = str(data_retrieved["contact"])
	company_mail = str(data_retrieved["mail"]).lower()
except:
	print("App opened first time so leaving company details")
