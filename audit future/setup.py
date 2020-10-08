import os
from styling import app_path
required_packages = ["matplotlib","datetime","termcolor","pillow","pyrebase","pyrebase4","xlsxwriter","kivy","pygame","babel"]
i = 0
not_installed = []
for element in required_packages:
    try:
        os.system(''.join(("pip install ",element)))
    except:
        i += 1
        not_installed.append(element)
print("No of modules couldn't be installed: ",i)
print("Modules which couldn't be installed:",not_installed)
print("This data is not a hundred percent accurate so check the terminal/cmd output for errors and try reinstalling it")
print("Starting app")
try:
	os.system(''.join(("python ",app_path)))
except:
	print("Couldn't open file try opening it manually")
