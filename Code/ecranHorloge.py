from tkinter import *
from time import *
from math import *

cptMs = 0.0
##Objects
aigSec = False
affHeu = False
Canevas = False
Fenetre = False

def animeAigSec():
    global aigSec
    global affHeu
    global cptMs
    global Canevas
    global Fenetre
    cptMs += 0.24
    rad = radians(cptMs)
    posX = cos(rad) * 230 + 640
    posY = sin(rad) * 230 + 300
    Canevas.coords(aigSec, 640, 300, posX, posY)
    current = localtime()
    sortie = convertdate(current)
    Canevas.itemconfig(affHeu, text=sortie)
    Canevas.after(40, animeAigSec)

def convertdate(current):
    annee = str(current[0])
    mois = str(current[1])
    journ = str(current[2])
    heure = str(current[3])
    minutes = str(current[4])
    secondes = str(current[5])
    jour = str(current[6])
    if current[5] < 10:
        secondes = '0' + secondes
    if current[4] < 10:
        minutes = '0' + minutes
    if current[3] < 10:
            heure = '0' + heure
    if current[6] == 0:
        jour = "Lundi"
    elif current[6] == 1:
        jour = "mardi"
    elif current[6] == 2:
        jour = "Mercredi"
    elif current[6] == 3:
        jour = "Jeudi"
    elif current[6] == 4:
        jour = "Vendredi"
    elif current[6] == 5:
        jour = "Samedi"
    elif current[6] == 6:
        jour = "Dimanche"
    if current[1] == 1:
        mois = "Janvier"
    elif current[1] == 2:
        mois = "Février"
    elif current[1] == 3:
        mois = "Mars"
    elif current[1] == 4:
        mois = "Avril"
    elif current[1] == 5:
        mois = "Mai"
    elif current[1] == 6:
        mois = "Juin"
    elif current[1] == 7:
        mois = "Juillet"
    elif current[1] == 8:
        mois = "Août"
    elif current[1] == 9:
        mois = "Septembre"
    elif current[1] == 10:
        mois = "Octobre"
    elif current[1] == 11:
        mois = "Novembre"
    elif current[1] == 12:
        mois = "Décembre"

    sortie = heure + ':' + minutes + ':' + secondes + '\n' + jour + ' ' + journ + ' ' + mois + ' ' + annee
    return sortie

def Horloge():
    global Fenetre
    global Canevas
    global aigSec
    global affHeu
    Fenetre = Tk()

    Canevas = Canvas(Fenetre, width=1280, height=1024, bg ='black')
    Canevas.pack(padx=0, pady=0)
    Canevas.create_oval(390, 50, 890, 550, outline='white', width="5", fill='black')
    Canevas.create_line(640, 300, 840, 300, fill="white", width="5")
    Canevas.create_line(640, 300, 640, 200, fill="white", width="10")
    aigSec = Canevas.create_line(640, 300, 640, 530, fill="red", width="2")
    affHeu = Canevas.create_text(700, 600, fill="white")

    Canevas.create_oval(630, 290, 650, 310, outline='white', width="5", fill='white')

    animeAigSec()
    Fenetre.mainloop()