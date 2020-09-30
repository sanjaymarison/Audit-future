from tkinter import messagebox
import os
import shutil
from styling import *

def create_backup():
        try:
            try:
                os.mkdir(backup_path)
            except:
                pass

            shutil.copyfile(DEFAULT_PATH, backup_path_file)
            messagebox.showinfo("Sucess","Backup sucessful")
            
        except:
            messagebox.showinfo("Unsucessful","Backup Unsucessful")
            