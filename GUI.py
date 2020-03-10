from tkinter import *


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


mgui = Tk()
mgui.title('Vote')
var1 = IntVar()
Checkbutton(mgui, text='Option 1', variable=var1, padx=mgui.winfo_screenwidth()/2).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(mgui, text='Option 2', variable=var2, padx=mgui.winfo_screenwidth()/2).grid(row=1, sticky=W)
Button(mgui, text='Submit', command=mgui.quit, padx=mgui.winfo_screenwidth()/2).grid(row=3, sticky=W, pady=4)
app = FullScreenApp(mgui)
mgui.mainloop()