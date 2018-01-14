from tkinter import *
from time import *

format = False

def horloge():
    current = localtime()
    sortie = convertdate(current)
    Label1["text"] = sortie
    Label1.after(1000, horloge)

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
    global Format
    if format == True:
        if current[3] < 12:
            heure = 'AM ' + heure
        else:
            heure = 'PM ' + str(current[3] - 12)
    else:
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
        jour = "Vendredii"
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

def format():
    global format
    if format == True:
        format = False
    else:
        format = True

Mafenetre = Tk()
Label1 = Label(Mafenetre, text="Horloge numérique", bg="black", fg="white", width="500", height="200", font="Ubuntu 100")
Label1.pack()
menubar = Menu(Mafenetre)

#c = Canvas(Mafenetre,)
#c.pack()
#fond = PhotoImage(file="background1.jpg")
#c.create_image(0, 0, image=fond)
#root = Tk()
#image = PhotoImage(file='background1.jpg', master=root)
#canvas = Canvas(root, width=500, height=500)
#canvas.pack()

#canvas.create_image((w//2, h//2), image=image)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="AM/PM", command=format)
menubar.add_cascade(label="Format", menu=menu1)

Mafenetre.config(menu=menubar)

horloge()
Mafenetre.mainloop()