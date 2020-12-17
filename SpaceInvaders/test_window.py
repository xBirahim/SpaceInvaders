from tkinter import *




mainwindow = Tk()
mainwindow.title("Space Invaders 2020")

gameplace = Frame(mainwindow)
gameplace.pack()

place = Canvas(gameplace,
               width=1000,
               height=800,
               bg="grey")
place.pack()


place.create_image(0, 0, image="Images/space.png")

mainwindow.mainloop()
