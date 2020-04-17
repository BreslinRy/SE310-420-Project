#    Anna Stoneman
#    Voting App Project, Login Module

#imports
import tkinter as tk


#file op function defs
def searchUsernameExist(username):
    found = 0
    data = open("userList.txt", "r")
    for line in data:
        if username in line:
            found = 1
    return found
    data.close()
    
def compPass(username, password):
    correct = 0
    data = open("userList.txt", "r")
    for line in data:
        if username in line:
            actPass = next(data)
            #actPass = line
            if (actPass == password+"\n"):
                correct = 1
                line = next(data)
                #if user is admin, correct = 2
                correct = correct+int(line)
    data.close()
    return correct

def newUser(username, password, admin):
    data = open("userList.txt", "a+")
    count = 0
    for line in data:
        count = count+1
    data.write(username+"\n")
    data.write(password+"\n")
    data.write(admin+"\n\n")
    data.close()

#button defs
def newUserClicked():
    newUserButton.destroy()
    returningUserButton.destroy()
    greeting.configure(text = "Clicked new user")
    newNormUserButton.grid(row=3, column=1)
    newAdminButton.grid(row=3, column=0)
    
def newAdminClicked():
    newAdminButton.destroy()
    newNormUserButton.destroy()
    greeting.configure(text="What is the admin password?")
    adminPassEntry.grid(row=3, column =0)
    adminPassEnterButton.grid(row=3, column=1)

def checkAdminPass():
    adminPassIn = adminPassEntry.get()
    if (adminPassIn == "we rule"):
        greeting.configure(text="Correct")
    else:
        greeting.configure(text="Incorrect")

def newNormUserClicked():
    newAdminButton.destroy()
    newNormUserButton.destroy()
    greeting.configure(text="What do you want your username to be?")
    usernameEntry.grid(row=3, column=0)
    newUserEnterButton.grid(row=3,column=1)

def newUserEnterClicked():
    global userIn
    userIn = usernameEntry.get()
    existing = searchUsernameExist(userIn)
    if (existing == 0):
        greeting.configure(text="What do you want your password to be?")
        usernameEntry.destroy()
        newUserEnterButton.destroy()
        newPassEntry.grid(row=3, column=0)
        newPassEnterButton.grid(row=3, column=1)
    elif (existing == 1):
        greeting.configure(text="Sorry that username already exists")

def newPassEnterClicked():
    #newPass = newPassEntry.get()
    userIn = "defaultuserid"
    newPass = "defaultpass"
    newUser(userIn, newPass, "0")
    greeting.configure(text="you're in!")
    
        
def returningUserClicked():
    newUserButton.destroy()
    returningUserButton.destroy()
    greeting.configure(text = "Clicked returning user")
    usernameEntry.grid(row=3, column=1)
    passEntry.grid(row=4, column=1)
    userLabel.grid(row=3, column=0)
    passLabel.grid(row=4, column=0)
    returnEnterButton.grid(row=5,column=1)

def returnEnterClicked():
    userIn = usernameEntry.get()
    passIn = passEntry.get()
    passReturn = compPass(userIn, passIn)
    if (passReturn == 0):
        greeting.configure(text = "incorrect username or password")
    elif (passReturn == 1):
        greeting.configure(text = "welcome ")
        returnEnterButton.destroy()
        usernameEntry.destroy()
        passEntry.destroy()
        userLabel.destroy()
        passLabel.destroy()
    elif (passReturn == 2):
        greeting.configure(text = "welcome admin ")
        usernameEntry.destroy()
        passEntry.destroy()
        returnEnterButton.destroy()
        passLabel.destroy()
        userLabel.destroy()
    
#tkinter stuff for creating a window
window = tk.Tk()
window.title("Voting App")
window.geometry('350x200')
greeting = tk.Label(text = "Are you a new or returning user?")
space = tk.Label(text = " ")

#button creates
newUserButton = tk.Button(
    text = "New User",
    width = 15,
    height = 2,
    bg = "black",
    fg = "white",
    command = newUserClicked
)

returningUserButton = tk.Button(
    text = "Returning User",
    width = 15,
    height = 2,
    bg = "black",
    fg = "white",
    command = returningUserClicked
)

newAdminButton = tk.Button(
    text = "New Admin User",
    width = 15,
    height = 2,
    bg = "black",
    fg = "white",
    command = newAdminClicked
)

adminPassEnterButton = tk.Button(
    text = "Enter",
    width = 15,
    height = 2,
    bg = "black",
    fg = "white",
    command = checkAdminPass
)

returnEnterButton = tk.Button(
    text = "Enter",
    width = 15,
    height = 2,
    bg = "black",
    fg = "white",
    command = returnEnterClicked
)

newNormUserButton = tk.Button(
    text = "New User",
    width = 15,
    height = 2,
    bg = "black",
    fg = "white",
    command = newNormUserClicked
)

newUserEnterButton = tk.Button(
    text = "Enter",
    width = 15,
    height = 2,
    bg = "black",
    fg = "white",
    command = newUserEnterClicked
)

newPassEnterButton = tk.Button(
    text = "Enter",
    width = 15,
    height = 2,
    bg = "black",
    fg = "white",
    command = newPassEnterClicked()
)

#entry creates
usernameEntry = tk.Entry(window, width=20)
passEntry = tk.Entry(window, width=20)
adminPassEntry = tk.Entry(window, width=20)
usernameEntry = tk.Entry(window, width=20)
newPassEntry = tk.Entry(window, width=20)

#label creates
userLabel = tk.Label(text = "Username: ")
passLabel = tk.Label(text = "Password: ")

#default setup
greeting.grid(row=0, column=0)
space.grid(row=1, column=0)
newUserButton.grid(row=3, column=0)
returningUserButton.grid(row=3, column=1)
window.mainloop()
