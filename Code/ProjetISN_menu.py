from tkinter import*
from tkinter.messagebox import *

menubar = False
fenetre = False

def a():
    showwarning('Inaccessible :(')

def removecontent():
    i = 0
    global fenetre
    global menubar
    for child in fenetre.winfo_children():
        if child != menubar:
            child.destroy()
        i += 1

def changer_date():

    global fenetre
    removecontent()

    Frame_chdate = Frame(fenetre)
    Frame_chdate.pack(pady=5, padx=15)

    Frame_jour = Frame(Frame_chdate, width=45, bg="grey")
    Frame_jour.pack(pady=5)

    Frame_mois = Frame(Frame_chdate, width=45, bg="grey")
    Frame_mois.pack(pady=5)

    Frame_annee = Frame(Frame_chdate, width=45, bg="grey")
    Frame_annee.pack(pady=5)

    label_jour = Label(Frame_jour, text="Jour", bg="grey")
    label_jour.pack(side=LEFT, padx=30)

    _jour = Spinbox(Frame_jour, from_=0, to=23, width=8)
    _jour.pack(side=RIGHT)

    label_mois = Label(Frame_mois, text="Mois", bg="grey")
    label_mois.pack(side=LEFT, padx=28)

    _mois = Spinbox(Frame_mois, from_=0, to=59, width=8)
    _mois.pack(side=RIGHT)

    label_annee = Label(Frame_annee, text="Année", bg="grey")
    label_annee.pack(side=LEFT, padx=24)

    _annee = Spinbox(Frame_annee, from_=0, to=59, width=8)
    _annee.pack(side=RIGHT)

    bouton=Button(fenetre, pady=6, text="Enregistrer", command=a)
    bouton.pack()

def changer_heure():

    global fenetre
    removecontent()

    Frame_chheure = Frame(fenetre)
    Frame_chheure.pack(pady=5, padx=15)

    Frame_heure = Frame(Frame_chheure, width=45, bg="grey")
    Frame_heure.pack(pady=5)

    Frame_min = Frame(Frame_chheure, width=45, bg="grey")
    Frame_min.pack(pady=5)

    Frame_sec = Frame(Frame_chheure, width=45, bg="grey")
    Frame_sec.pack(pady=5)

    label_heure = Label(Frame_heure, text="Heures", bg="grey")
    label_heure.pack(side=LEFT, padx=22)

    _heure = Spinbox(Frame_heure, from_=0, to=23, width=8)
    _heure.pack(side=RIGHT)

    label_min = Label(Frame_min, text="Minutes", bg="grey")
    label_min.pack(side=LEFT, padx=19)

    _min = Spinbox(Frame_min, from_=0, to=59, width=8)
    _min.pack(side=RIGHT)

    label_sec = Label(Frame_sec, text="Secondes", bg="grey")
    label_sec.pack(side=LEFT, padx=15)

    _sec = Spinbox(Frame_sec, from_=0, to=59, width=8)
    _sec.pack(side=RIGHT)

    bouton=Button(fenetre, pady=6, text="Enregistrer", command=a)
    bouton.pack()



def aff():

    global fenetre
    removecontent()

    phrase = StringVar()
    phrase.set("texte par défaut")
    entree = Entry(fenetre, width=30)
    entree.pack()

    liste = Listbox(fenetre, height=4)
    liste.insert(1, "Jaune")
    liste.insert(2, "Rouge")
    liste.insert(3, "Vert")
    liste.insert(4, "Bleu")
    liste.pack(pady=3)

    bouton=Button(fenetre, pady=6, text="Enregistrer", command=a)
    bouton.pack()

def load_dashboardwindows(window):

    global menubar
    global fenetre

    fenetre = window

    removecontent()
    fenetre.title('Horloge')
    menubar = Menu(fenetre)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Changer la date", command=changer_date)
    menu1.add_command(label="Changer l'heure", command=changer_heure)
    menu1.add_command(label="Afficher une phrase", command=aff)
    menu1.add_separator()
    menu1.add_command(label="Relancer", command=a)
    menubar.add_cascade(label="Parametres", menu=menu1)

    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="Informations", command=a)

    menubar.add_cascade(label="Aide", menu=menu2)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="Fermer la fenêtre", command=fenetre.quit)
    menubar.add_cascade(label="Quitter", menu=menu3)
    fenetre.config(menu=menubar)