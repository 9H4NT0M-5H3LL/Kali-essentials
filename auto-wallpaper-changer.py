#!/usr/bin/python3
import os
import random

wall_names = []
count = 0                                                         #variable to add files in the current directory
for root, dirs, files in os.walk("/home/mr-robot/Pictures/desktop/."):     #change the directory to your specified one
    for filename in files:
        wall_names.append(filename)
        count = count+1
    #print(wall_names)
#print(count)
if count != 0:
    wall_no = random.randrange(1,count+1,1)
    wallpaper = wall_names[wall_no-1]
    #print(wall_no, wallpaper)
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/mr-robot/Pictures/desktop/" + "\'" + wallpaper + "\'")
    exit()
else:
    import tkinter as tk
    from tkinter import ttk
    from tkinter.messagebox import showinfo
    def popup_bonus():
        win = tk.Toplevel()
        win.wm_title("System_Message")
        l = tk.Label(win, text="Input")
        l.grid(row=0, column=0)
        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.grid(row=1, column=0)
    def popup_showinfo():
        showinfo("System Message", "Your wallpaper directory is empty! Add some images to set wallpapers automatically upon next boot.")
    class Application(ttk.Frame):
        def __init__(self, master):
            ttk.Frame.__init__(self, master)
            self.pack()
            self.button_showinfo = ttk.Button(self, text="System Warning!, non-critical\n Press here for more info", command=popup_showinfo)
            self.button_showinfo.pack()
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
