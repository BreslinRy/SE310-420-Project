#   Rylie Breslin
#   SE420 Assignment 4
from tkinter import *
from Count import count

#   Taken from user Unutbu on Stack Overflow
#   Resizes the GUI to full screen
#   Press escape to toggle the size between default and full screen
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
vote = IntVar()     # Will allow us to tell if this option was checked

# Creating a checkbox(tkinter name, candidate option, save state of box location, location on screen)
Radiobutton(mgui, text='John Johnson', variable=vote, value = 1, padx=mgui.winfo_screenwidth()/2).grid(row=0, sticky=W)
# Creating a checkbox(tkinter name, candidate option, save state of box location, location on screen)
Radiobutton(mgui, text='Sam Samson', variable=vote, value=2, padx=mgui.winfo_screenwidth()/2).grid(row=1, sticky=W)

# Creating a button(tkinter instance, Button text, what function the button calls, location on screen)
button = Button(mgui, text='Submit', command=mgui.quit, padx=mgui.winfo_screenwidth()/2).grid(row=3, sticky=W, pady=4)

app = FullScreenApp(mgui)       # Calls function to make the gui full screen
mgui.mainloop()     # Creates the GUI

count(vote.get())   # Counts the votes for each applicant