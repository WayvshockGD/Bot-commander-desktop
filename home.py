#modules
from tkinter import *
from PIL import Image, ImageTk
from assets.resources.strings import *
from assets.resources.colors import *
from src.styles import *

#####################
#code

root = Tk()
root.title('BCFD desktop')
root.geometry("1300x700")


icon = PhotoImage(file ="assets/BCFD-LOGO.png")
root.iconphoto(True, icon)

title = Label(root, text=bcfdText, anchor='w',bg = barColor, fg = white)

title.pack(fill = "x")

img = ImageTk.PhotoImage(Image.open("assets/BCFD-Default-icon.png"))
panel = Label(root, anchor='n', image = img, bg=imgBackroundColor)
panel.pack(fill = "both", expand = "yes")

tokenBox = Entry(root, width="55", text=tokenText)
tokenBox.pack(expand = "yes", anchor="center", side='top')

root.configure(bg=color)

#######################
#on


root.mainloop()





