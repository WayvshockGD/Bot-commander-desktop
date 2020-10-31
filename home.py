#modules
from tkinter import *

#####################
#text i guess

bcfdText = "Bot Commander Desktop"

#####################
#code

root = Tk()
root.title('BCFD desktop')
root.geometry("1300x700")

icon = PhotoImage(file = "BCFD-LOGO.png")
root.iconphoto(True, icon)



title = Label(root, text=bcfdText, anchor='w')

title.pack(fill = "x")

tokenBox = Entry(root, width=50)
tokenBox.pack()

#######################

#on

root.mainloop()