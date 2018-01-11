from tkinter import*
from tkinter.messagebox import *

def a():
    showwarning('Inaccessible :(')

def ch_heure():

    Frame_ch_heure = Frame(fenetre)
    Frame_ch_heure.pack()

    l_heure = LabelFrame(Frame_ch_heure, text="Heures", padx=20, pady=20)
    l_heure.pack(side=LEFT, padx=3)

    l_min = LabelFrame(Frame_ch_heure, text="Minutes", padx=20, pady=20)
    l_min.pack(side=LEFT, padx=3)

    l_sec = LabelFrame(Frame_ch_heure, text="Secondes", padx=20, pady=20)
    l_sec.pack(side=LEFT, padx=3)

    _heure = DoubleVar()
    scale = Scale(l_heure, variable=_heure, from_=0, to=24)
    scale.pack(side=LEFT)

    _min = DoubleVar()
    scale = Scale(l_min, variable=_min, from_=0, to=59)
    scale.pack(side=LEFT)

    _sec = DoubleVar()
    scale = Scale(l_sec, variable=_sec, from_=0, to=59)
    scale.pack(side=LEFT)

    bouton=Button(fenetre, pady=6, text="Enregistrer", command=a)
    bouton.pack()

def ch_date():

    Frame_ch_date = Frame(fenetre)
    Frame_ch_date.pack()

    l_mois = LabelFrame(Frame_ch_date, text="Mois", padx=20, pady=20)
    l_mois.pack(side=LEFT, padx=3)

    l_jour = LabelFrame(Frame_ch_date, text="Jour", padx=20, pady=20)
    l_jour.pack(side=LEFT, padx=3)

    l_annee = LabelFrame(Frame_ch_date, text="Année", padx=20, pady=20)
    l_annee.pack(side=LEFT, padx=3)

    _mois = DoubleVar()
    scale = Scale(l_mois, variable=_mois, from_=1, to=12)
    scale.pack(side=LEFT)

    _jour = DoubleVar()
    scale = Scale(l_jour, variable=_jour, from_=1, to=31)
    scale.pack(side=LEFT)

    _annee = DoubleVar()
    scale = Scale(l_annee, variable=_annee, from_=18, to=58)
    scale.pack(side=LEFT)

    bouton=Button(fenetre, pady=6, text="Enregistrer", command=a)
    bouton.pack()

def aff():

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

def load_dashboardwindows(fenetre):
    fenetre.title('Horloge')

    menubar = Menu(fenetre)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Changer la date", command=ch_date)
    menu1.add_command(label="Changer l'heure", command=ch_heure)
    menu1.add_command(label="Afficher une phrase", command=aff)
    menu1.add_separator()
    menu1.add_command(label="Relancer", command=a)
    menubar.add_cascade(label="Parametres", menu=menu1)

    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="A propos", command=a)
    menu2.add_command(label="Fiche explicative", command=a)

    menubar.add_cascade(label="Aide", menu=menu2)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="Fermer la fenêtre", command=fenetre.quit)
    menubar.add_cascade(label="Quitter", menu=menu3)
    fenetre.config(menu=menubar)

##fenetre.mainloop()
