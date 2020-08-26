import tkinter as tk
from tkinter import filedialog, Text
import subprocess
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="selectfile",
                                          filetypes=(("executables", "*.app"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, fg="#BDBDBD")
        label.pack()


def runApps():
    for app in apps:
        subprocess.run(["open", app])


canvas = tk.Canvas(root, height=700, width=700, bg="#ece1ea")
canvas.pack()

canvas.create_text(350, 40, fill="#8C8B8B",
                   font="Times 20 italic bold", text="Little GUI App")

frame = tk.Frame(root, bg="#f7f3f7")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=10,
                     fg="#BDBDBD", bg="#ece1ea", command=addApp)
openFile.pack()

openFile = tk.Button(root, text="Run Apps", padx=10,
                     pady=10, fg="#BDBDBD", bg="#ece1ea", command=runApps)
openFile.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
