import tkinter as tk
from tkinter import filedialog, Text, simpledialog
import os
import pickle
from PIL import Image, ImageTk
from tkinter import *


indir = "/"
apps = {
    "0":[],
    "1":[],
    "2":[],
    "3":[],
    "4":[],
    "5":[],
    "6":[],
    "7":[],
    "8":[],
    "9":[],
    "10":[],
    "11":[],
    "12":[],
    "13":[],
    "14":[],
    "15":[],
    "16":[],
    "17":[],
    "18":[],
    "19":[],
    "20":[],
    "21":[],
    "22":[],
    "23":[],
}
admin = {
    "admin": True,
    "password": "Panda"
}


def save_obj(apps):
    with open('apps.pkl', 'wb') as f:
        pickle.dump(apps, f, pickle.HIGHEST_PROTOCOL)


def load_obj():
    with open('apps.pkl', 'rb') as f:
        return pickle.load(f)


def load_admin():
    with open('admin.pkl', 'rb') as f:
        return pickle.load(f)

def save_admin(admin):
    with open('admin.pkl', 'wb') as f:
        pickle.dump(admin, f, pickle.HIGHEST_PROTOCOL)


apps = load_obj()
admin = load_admin()


def addapp():
    global programs
    if admin.get("admin") == True:
        filename = filedialog.askopenfilename(initialdir=f"{indir}", title="Select App", parent=root, filetypes=(("executables", "*.exe"),("all files", "*")))
        if filename is not "":
            timePopup = simpledialog.askinteger(title="Time", prompt="When should this be executed?")
            tempApp = apps.get(f"{timePopup}")
            tempApp.append(filename)
            apps.update({f"{timePopup}": tempApp})
            programs.delete(first=0, last="end")
            for element in apps:
                tempApp = apps.get(f"{element}")
                for app in tempApp:
                    programs.insert(END, f"{element}:00 {app}")
            programs.pack(side="left", fill="both")
        save_obj(apps)
    else:
        adminPopup = simpledialog.askstring(title="Password", prompt="Please enter the admin password:")
        if adminPopup == admin.get("password"):
            filename = filedialog.askopenfilename(initialdir=f"{indir}", title="Select App", parent=root,
                                                  filetypes=(("executables", "*.exe"), ("all files", "*")))
            if filename is not "":
                timePopup = simpledialog.askinteger(title="Time", prompt="When should this be executed?")
                tempApp = apps.get(f"{timePopup}")
                tempApp.append(filename)
                apps.update({f"{timePopup}": tempApp})
                programs.delete(first=0, last="end")
                for element in apps:
                    tempApp = apps.get(f"{element}")
                    for app in tempApp:
                        programs.insert(END, f"{element}:00 {app}")
                programs.pack(side="left", fill="both")
            save_obj(apps)


def runapp():
    for element in apps:
        tempapp = apps.get(f"{element}")
        for app in tempapp:
            print(app)
            os.startfile(app)


def delapp():
    global apps, programs
    if admin.get("admin") == True:
        apps = {
            "0":[],
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [],
            "9": [],
            "10": [],
            "11": [],
            "12": [],
            "13": [],
            "14": [],
            "15": [],
            "16": [],
            "17": [],
            "18": [],
            "19": [],
            "20": [],
            "21": [],
            "22": [],
            "23": [],
        }
        save_obj(apps)
        load_obj()
        programs.delete(first=0, last="end")
    else:
        adminPopup = simpledialog.askstring(title="Password", prompt="Please enter the admin password:")
        if adminPopup == admin.get("password"):
            apps = {
                "0": [],
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": [],
                "6": [],
                "7": [],
                "8": [],
                "9": [],
                "10": [],
                "11": [],
                "12": [],
                "13": [],
                "14": [],
                "15": [],
                "16": [],
                "17": [],
                "18": [],
                "19": [],
                "20": [],
                "21": [],
                "22": [],
                "23": [],
            }
            save_obj(apps)
            load_obj()
            programs.delete(first=0, last="end")

def close():
    exit()


root = tk.Tk()
screenwith = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
canvas = tk.Canvas(root, height=screenheight, width=screenwith, bg="white",)
canvas.pack()
root.iconbitmap("Startup.ico")
root.title("StartUp V0.7")

frame3 = tk.Frame(root, bg="#DDDDDD")
frame3.place(relwidth=1, relheight=0.05)

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=1, relx=0.2, rely=0.05)

frame2 = tk.Frame(root, bg="#EBEDEE")
frame2.place(relwidth=0.2, relheight=1, rely=0.05)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

programs = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=500, bd=0)
programs.pack(side="left", fill="both")


#logo = Image.open("Startup.png")
#logo = ImageTk.PhotoImage(logo)
#logoImage = tk.Label(frame3, image=logo)
#logoImage.image = logo
#logoImage.grid()

text = tk.Label(frame3, fg="#545454", font=("Verdana", 10), bd=0, bg="#DDDDDD", text="StartUp Alpha 0.7", pady=10)
text.grid(sticky="W")

close = tk.Button(frame3, text='X', bd=0, fg="#545454", bg="#DDDDDD", command=close)
close.grid(row=0, column=1, sticky='W')

openFiles = tk.Button(frame2, text="Open Files", padx=20, pady=10, fg="black", bg="#EBEDEE", command=addapp,
                      font="Verdana", bd=0, activebackground="#E1E1E1")
openFiles.grid(row=0, column=0, sticky="W")

runApps = tk.Button(frame2, text="Run all Apps", padx=18, pady=10, fg="black", bg="#EBEDEE", command=runapp,
                    font="Verdana", bd=0, activebackground="#E1E1E1")
runApps.grid(row=1, column=0, sticky="W")

deleteApps = tk.Button(frame2, text="Delete Apps", padx=14, pady=10, fg="black", bg="#EBEDEE", command=delapp,
                       font="Verdana", bd=0, activebackground="#E1E1E1")
deleteApps.grid(row=2, column=0, sticky="W")

for element in apps:
    tempApp = apps.get(f"{element}")
    for app in tempApp:
        programs.insert(END, f"{element}:00 {app}")
programs.pack(side="left", fill="both")


root.mainloop()

save_obj(apps)
save_admin(admin)
