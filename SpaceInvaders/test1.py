from tkinter import *
from os import path

velocity = 4


class Ennemy:

    def __init__(self, main, xcor, ycor):
        self.health = 100
        pass


class Player:

    def __init__(self, xcor, ycor, health=100):
        self.xcor = xcor
        self.ycor = ycor
        self.health = health
        self.lasers = []
        self.cooldown = 0
        self.rep = place.coords(player,self.xcor - 10, self.ycor - 10, self.xcor + 10, self.ycor + 10)

    def draw(self):
        #place.coords(player, self.xcor, self.ycor)
        pass

    def move(self, event):
        """ Gestion de l'événement Appui sur une key du clavier """
        key = event.keysym
        print(key)
        # déplacement vers la droite
        if key == 'd':
            self.xcor += 20
        # déplacement vers la gauche
        if key == 'a':
            self.xcor -= 20
        # on dessine le pion à sa nouvelle position
        place.coords(self.rep, self.xcor - 10, self.ycor - 10, self.xcor + 10, self.ycor + 10)
        print(self.rep)


class Laser:

    def __init__(self, xcor, ycor):
        self.xcor = xcor
        self.ycor = ycor
        self.image = PhotoImage(path.join("assets", "laser_green.png"))

    def draw(self, canvas):
        #  canvas.create_image(self.xcor, self.ycor, image=self.image)
        canvas.create_oval(self.xcor - 10, self.ycor - 10, self.xcor + 10, self.ycor + 10,
                           width=5, outline='black', fill='red')

    def move(self, canvas, velocity):
        self.ycor += velocity
        canvas.coords(self.rep, self.xcor - 10, self.ycor, self.xcor + 10, self.ycor)


mainwindow = Tk()
mainwindow.title("Space Invaders 2020")

gameplace = Frame(mainwindow)
gameplace.pack()

place = Canvas(gameplace,
               width=1000,
               height=800,
               bg='grey')

Fond = PhotoImage(file='Images/space.png')
place.create_image(0, 0, anchor=NW, image=Fond)
#Player
PosX = 70
PosY = 70
imageplayer= PhotoImage(file='Images/player.png')
player= place.create_image(PosX, PosY, image=imageplayer)
# Aliens
sizeAlien = 30
Alien = place.create_rectangle(0, 0, sizeAlien*2, sizeAlien*2, fill='green')
X = 0
Y = 0
dX = 10
dY = 0
place.move(Alien,dX,dY)
place.pack()


#player = Player(xcor=900, ycor=400)
#player.draw()
#place.focus_set()
#place.bind("<Key>", player.move)

mainwindow.mainloop()
