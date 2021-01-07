from tkinter import *
from os import path

velocity = 4
wwidth = 1000
wheight = 800


class Ennemy:

    def __init__(self, xcor=500, ycor=200):
        self.xcor = xcor
        self.ycor = ycor
        self.velocity = 10
        self.health = 100
        self.lasers = []
        self.rep = place.create_oval(self.xcor - 10, self.ycor - 10, self.xcor + 10, self.ycor + 10,
                                     width=5, outline='green', fill='blue')

        self.move()

    def move(self):
        self.xcor += self.velocity
        if self.xcor < 0 or self.xcor > 1000:
            self.ycor += 40
            self.velocity *= -1

        place.coords(self.rep, self.xcor - 10, self.ycor - 10, self.xcor + 10, self.ycor + 10)

        try:
            mainwindow.after(50, self.move)
        except TclError:
            print("Bruh")


class Player:

    def __init__(self, xcor, ycor, health=100):
        self.xcor = xcor
        self.ycor = ycor
        self.health = health
        self.lasers = []
        self.cooldown = 0
        self.rep = place.create_oval(self.xcor - 10, self.ycor - 10, self.xcor + 10, self.ycor + 10)

        self.cleanlasers()

    def action(self, event):
        """ Gestion de l'événement Appui sur une key du clavier """
        key = event.keysym
        print(key)
        # déplacement vers la droite
        if key == 'd':
            self.xcor += 20
            if self.xcor > 1000:
                self.xcor = 1000

        # déplacement vers la gauche
        if key == 'a':
            self.xcor -= 20
            if self.xcor < 0:
                self.xcor = 0

        # on dessine le pion à sa nouvelle position
        place.coords(self.rep, self.xcor - 10, self.ycor - 10, self.xcor + 10, self.ycor + 10)

        if key == 'space':
            print("shoot")
            laser = Laser(xcor=self.xcor, ycor=self.ycor - 10)
            self.lasers += [laser]

    def cleanlasers(self):

        deleted = []

        for laser in self.lasers:
            if not -100 < laser.ycor < 1100:
                print("laser popped out")
                laser.destroy()
                deleted.append(laser)

        self.lasers = [item for item in self.lasers if item not in deleted]

        try:
            mainwindow.after(5000, self.cleanlasers)
        except TclError:
            print("Bruh")


class Laser:

    def __init__(self, xcor, ycor):
        self.velocity = 4
        self.xcor = xcor
        self.ycor = ycor
        # self.image = PhotoImage(path.join("assets", "laser_green.png"))
        self.rep = place.create_oval(self.xcor - 10, self.ycor - 10, self.xcor + 10, self.ycor + 10,
                           width=5, outline='blue', fill='blue')

        self.move()

    def draw(self, canvas):
        #  canvas.create_image(self.xcor, self.ycor, image=self.image)
        canvas.create_oval(self.xcor - 10, self.ycor - 10, self.xcor + 10, self.ycor + 10,
                           width=5, outline='black', fill='blue')

    def move(self):

        self.ycor -= 5
        place.coords(self.rep, self.xcor - 10, self.ycor, self.xcor + 10, self.ycor)
        try:
            mainwindow.after(10, self.move)
        except TclError:
            print("Bruh")

    def destroy(self):
        pass


mainwindow = Tk()
mainwindow.title("Space Invaders 2020")

gameplace = Frame(mainwindow)
gameplace.pack()

place = Canvas(gameplace,
               width=wwidth,
               height=wheight,
               bg="grey")
Fond = PhotoImage(file='Images/space.png')
place.create_image(0,0,anchor=NW,image=Fond)
place.pack()

player = Player(xcor=500, ycor=750)

place.focus_set()
place.bind("<Key>", player.action)

ennemy = Ennemy()



mainwindow.mainloop()
