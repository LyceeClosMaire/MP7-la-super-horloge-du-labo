from tkinter import *
from time import *
from math import *

cptAs = -90.0
cptTs = 0
cptAm = -90.0
cptTm = 0
cptAh = -90.0
cptTh = 0
##Objects
aigSec = False
aigMin = False
aigHeu = False
affHeu = False
affTIn = False
affTEx = False
Canevas = False
Fenetre = False

def animeAigSec():
    global aigSec
    global cptAs
    global Canevas

    cptAs += 0.24
    rad = radians(cptAs)
    posX = cos(rad) * 230 + 640
    posY = sin(rad) * 230 + 300
    Canevas.coords(aigSec, 640, 300, posX, posY)

def animeAigMin():
    global aigMin
    global cptAm
    global Canevas

    cptAm += 0.02
    rad = radians(cptAm)
    posX = cos(rad) * 230 + 640
    posY = sin(rad) * 230 + 300
    Canevas.coords(aigMin, 640, 300, posX, posY)

def animeAigHeu():
    global aigHeu
    global cptAh
    global Canevas

    cptAh += 0.25
    rad = radians(cptAh)
    posX = cos(rad) * 230 + 640
    posY = sin(rad) * 230 + 300
    Canevas.coords(aigHeu, 640, 300, posX, posY)

def animeTexHeu(heure):
    global affHeu
    global affTIn
    global affTEx
    global Canevas

    Canevas.itemconfig(affHeu, text=heure)
    Canevas.itemconfig(affTIn, text="27.5")
    Canevas.itemconfig(affTEx, text="13°c")

def gettime():
    current = localtime()
    return current

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

def createHorloge():
    global Fenetre
    global Canevas
    global aigSec
    global aigMin
    global aigHeu
    global affHeu
    global affTEx
    global affTIn

    Fenetre = Tk()

    Canevas = Canvas(Fenetre, width=1280, height=1024, bg ='black')
    Canevas.pack(padx=0, pady=0)
    Canevas.create_oval(390, 50, 890, 550, outline="white", fill="white", width="5")

    Canevas.create_line(640, 30, 640, 70, fill="black", width="3")
    Canevas.create_line(755, 101, 775, 67, fill="black", width="3")
    Canevas.create_line(839, 185, 873, 165, fill="black", width="3")
    Canevas.create_line(370, 300, 410, 300, fill="black", width="3")
    Canevas.create_line(839, 415, 873, 435, fill="black", width="3")
    Canevas.create_line(755, 499, 775, 533, fill="black", width="3")
    Canevas.create_line(640, 570, 640, 530, fill="black", width="3")
    Canevas.create_line(441, 415, 407, 435, fill="black", width="3")
    Canevas.create_line(525, 499, 505, 533, fill="black", width="3")
    Canevas.create_line(870, 300, 910, 300, fill="black", width="3")
    Canevas.create_line(441, 185, 407, 165, fill="black", width="3")
    Canevas.create_line(525, 101, 505, 67, fill="black", width="3")

    aigMin = Canevas.create_line(640, 300, 840, 300, fill="black", width="5")
    aigHeu = Canevas.create_line(640, 300, 640, 150, fill="black", width="8")
    aigSec = Canevas.create_line(640, 300, 640, 300, fill="red", width="2")
    Canevas.create_text(195, 250, fill="white", font="Montserrat 35", width="400", justify="center", text="INTERIEURE")
    Canevas.create_text(1085, 250, fill="white", font="Montserrat 35", width="400", justify="center", text="EXTERIEURE")
    affHeu = Canevas.create_text(640, 680, fill="white", font="Montserrat 60", width="1000", justify="center")
    affTIn = Canevas.create_text(195, 350, fill="white", font="Montserrat 120", width="400", justify="center")
    affTEx = Canevas.create_text(1085, 350, fill="white", font="Montserrat 120", width="400", justify="center")
    Canevas.create_oval(630, 290, 650, 310, outline="black", width="5", fill="black")

    return Fenetre

def horloge():
    global Fenetre
    global Canevas
    global cptTs
    global cptTm
    global cptTh
    global cptAs
    global cptAm
    global cptAh

    heure = gettime()

    if heure[5] == 0 or cptTs == 1500:
        cptAs = -90.0
        cptTs = 0
    elif cptTs % 5 == 0:
        cptTm =+ 1
        animeAigMin()
        animeTexHeu(convertdate(heure))
    elif cptTm % 30 == 0:
        cptTh =+ 1
        animeAigHeu()
    elif cptTm == 3600:
        cptAm = -90.0
        cptTm = 0
    elif cptTh == 720:
        cptAh = -90.0
        cptTh = 0

    animeAigSec()
    cptTs +=1
    Canevas.after(39, horloge)
