#   Rylie Breslin
#   SE420 Assignment 4
from tkinter import *
from Count import count


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

# def submit():
    # Interface with a database here


mgui = Tk()     # Setting tkinter equal to a callable name
mgui.title('Vote')      # Setting the title for the GUI
var1 = IntVar()     # Will allow us to tell if this option was checked
Checkbutton(mgui, text='John Johnson', variable=var1, padx=mgui.winfo_screenwidth()/2).grid(row=0, sticky=W)
# Creating a checkbox(tkinter name, candidate option, save state of box location, location on screen)
var2 = IntVar()     # Will allow us to tell if this option was checked
Checkbutton(mgui, text='Sam Samson', variable=var2, padx=mgui.winfo_screenwidth()/2).grid(row=1, sticky=W)
# Creating a checkbox(tkinter name, candidate option, save state of box location, location on screen)
Button(mgui, text='Submit', command=mgui.quit, padx=mgui.winfo_screenwidth()/2).grid(row=3, sticky=W, pady=4)
# Creating a button(tkinter instance, Button text, what function the button calls, location on screen)
app = FullScreenApp(mgui)       # Calls function to make the gui full screen
mgui.mainloop()     # Creates the GUI
count(var1.get(), var2.get())
