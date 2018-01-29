##imports
from tkinter import *
from time import *
from math import *

c = 0
inlineMess = ""
##Variables globales représentant des objets tkinter
aigSec = False
aigMin = False
aigHeu = False
affHeu = False
affTIn = False
affTEx = False
affHeu = False
Canevas = False
Fenetre = False
background = False
centre = False

##Fonctions d'affichage des aiguiles
def animeAigSec(secondes):
    ##On récupère les objets aiguilles et Canevas
    global aigSec
    global Canevas
    ##On calcul l'angle par rapport à l'origine du cercle trigo en fct du temps
    angle = radians(secondes * 6 - 90)
    ##On calcul l'extrémité en X et Y de l'aiguille
    posX = cos(angle) * 230 + 640
    posY = sin(angle) * 230 + 300
    ##On modifie les coordonnées de l'aiguille
    Canevas.coords(aigSec, 640, 300, posX, posY)

##Similaire à animeAigSec()
def animeAigMin(minutes):
    global aigMin
    global Canevas

    angle = radians(minutes * 6 - 90)
    posX = cos(angle) * 200 + 640
    posY = sin(angle) * 200 + 300
    Canevas.coords(aigMin, 640, 300, posX, posY)

##Similaire à animeAigSec()
def animeAigHeu(heures):
    global aigHeu
    global Canevas

    angle = radians(heures % 12 * 30 - 90)
    posX = cos(angle) * 150 + 640
    posY = sin(angle) * 150 + 300
    Canevas.coords(aigHeu, 640, 300, posX, posY)

##Affichage temps réel de l'heure/temp
def animeTexHeu(heure, temp):
    ##On récupère les objets tkinter
    global affHeu
    global affTIn
    global affTEx
    global Canevas
    ##On configure les objets label avec leur nouveau contenu
    heure = convertdate(heure)
    Canevas.itemconfig(affHeu, text=heure)
    ##temp = round(temp, 1)
    Canevas.itemconfig(affTIn, text=temp)
    Canevas.itemconfig(affTEx, text="13°c")

def animeMessage():
    ##On récupère les objets tkinter
    global Fenetre
    global Canevas
    global background
    global c
    global centre
    global affMess
    global inlineMess
    ##On modifie petit à petit la taille des éléments
    Canevas.coords(background, 640 - 250 - (c*10), 300 - 250 - (c*10), 640 + 250 + (c*10), 300 + 250 + (c*10))
    Canevas.itemconfigure(centre, fill="white", outline="white")
    Canevas.coords(centre, 640 - 10 - (c*10), 300 - 10 - (c*10), 640 + 10 + (c*10), 300 + 10 + (c*10))
    ##on incrémente le compteur
    c += 1
    message="test"
    ##longueur du message
    sizeMess = 60 + len(message)

    ##Si le compteur inf à 60, on contine l'animation d'agrandissement du cercle
    if c < 60:
        Canevas.after(5, animeMessage())
    ##Sinon On affiche le message lettre par lettre à chaque tour
    elif c < sizeMess:
        i = int(c-600)
        inlineMess = inlineMess + message[i]
        Canevas.itemconfig(affMess, text=inlineMess)
        Canevas.after(100, animeMessage())
    ##enfin on remet à zéro
    else:
        c = 0

def removeMessage():
    ##On récupère les objets tkinter
    global Canevas
    global background
    global centre
    global affMess
    ##On remet le message à zéro
    Canevas.coords(background, 390, 50, 890, 550,)
    Canevas.itemconfigure(centre, fill="black", outline="black")
    Canevas.coords(centre, 630, 290, 650, 310,)
    Canevas.itemconfig(affMess, text="")

def convertdate(current):
    ##conversion de la date en chaîne lisible
    annee = str(current[0])
    mois = str(current[1])
    journ = str(current[2])
    heure = str(current[3])
    minutes = str(current[4])
    secondes = str(current[5])
    jour = str(current[6])
    ##Chaque int du tableau fourni est comparé pour associer un jour/mois en lettres
    if current[5] < 10:
        secondes = '0' + secondes
    if current[4] < 10:
        minutes = '0' + minutes
    if current[3] < 10:
            heure = '0' + heure
    if current[6] == 0:
        jour = "Lundi"
    elif current[6] == 1:
        jour = "Mardi"
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

    ##on concatène la chaîne
    sortie = heure + ':' + minutes + ':' + secondes + '\n' + jour + ' ' + journ + ' ' + mois + ' ' + annee
    return sortie

def createHorloge():
    ##ON modifie les objets tkinter
    global Fenetre
    global Canevas
    global aigSec
    global aigMin
    global aigHeu
    global affHeu
    global affTEx
    global affTIn
    global background
    global centre
    global affMess

    Fenetre = Tk()
    ##fonctions du modules tkinter dpour la création
    Canevas = Canvas(Fenetre, width=1280, height=1024, bg ='black')
    Canevas.pack(padx=0, pady=0)
    background = Canevas.create_oval(390, 50, 890, 550, outline="white", fill="white", width="5")

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

    aigMin = Canevas.create_line(640, 300, 640, 100, fill="black", width="5")
    aigHeu = Canevas.create_line(640, 300, 640, 150, fill="black", width="8")
    aigSec = Canevas.create_line(640, 300, 640, 70, fill="red", width="2")
    Canevas.create_text(195, 250, fill="white", font="Montserrat 35", width="400", justify="center", text="INTERIEURE")
    Canevas.create_text(1085, 250, fill="white", font="Montserrat 35", width="400", justify="center", text="EXTERIEURE")
    affHeu = Canevas.create_text(640, 680, fill="white", font="Montserrat 60", width="1000", justify="center")
    affTIn = Canevas.create_text(195, 350, fill="white", font="Montserrat 120", width="400", justify="center")
    affTEx = Canevas.create_text(1085, 350, fill="white", font="Montserrat 120", width="400", justify="center")
    centre = Canevas.create_oval(630, 290, 650, 310, outline="black", width="5", fill="black")
    affMess = Canevas.create_text(630, 350, fill="black", font="Montserrat 80", width="1000", justify="center")

    return Fenetre, Canevas
