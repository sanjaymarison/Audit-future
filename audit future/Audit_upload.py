try:
    from tkinter import messagebox
    from styling import *
    import time
    import pyrebase
    from termcolor import colored
except:
    print(colored("Audit upload will not function until pyrebase module is installed","red"))

# to use the upload module start a firebase storage space and insert the details here
def upload_to_cloud():
    try:

        for i in range(1):
            config = {
                "apiKey": "",
                "authDomain": "",
                "databaseURL": "",
                "projectId": "",
                "storageBucket": "",
                "messagingSenderId": "",
                "appId": "",
                "measurementId": ""

            }


            email = ""
            password = ""

            path_on_cloud = "database/appdata.db"
            path_local = DEFAULT_PATH

            firebase = pyrebase.initialize_app(config)




            auth = firebase.auth()
            user = auth.sign_in_with_email_and_password(email,password)



            storage = firebase.storage()
            storage.child(path_on_cloud).put(path_local,user['idToken'])

            messagebox.showinfo("UPLOAD STATUS","UPLOAD SUCESSFUL")
    except:
        messagebox.showwarning("UPLOAD STATUS","UPLOAD UNSUCESSFUL")

      



    
