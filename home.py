#modules
from tkinter import *
from PIL import Image, ImageTk

#####################
#text i guess

bcfdText = "Bot Commander Desktop"

#####################
#colors

color = "#494949"
barColor = "#0C0C0C"
white = "#FFFFFF"

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
panel = Label(root, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")

root.configure(bg=color)

#######################
#on


root.mainloop()





