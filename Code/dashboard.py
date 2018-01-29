from tkinter import*            ##On importe différents modules qui seront utiles au programme
from tkinter.messagebox import *
import socket           ##Ce module permet, en particulier, de communiquer sur un réseau IP

menubar = False         ##On Initialise différentes varibles qui serviront au cours du programme
fenetre = False
cpt_clign = 0
cpt_delai = 0

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def a():            ##Fonction faisant apparaître un message désignant qu'un endroit de la page est inaccessible, devient inutile lorsque ce dernier est finit
    showwarning('Inaccessible :(')

def removecontent():            ##Fonction qui, lorsque que l'on désire changer de section à partir du menu, supprime le contenu déjà présent sur la page
    global fenetre          ##Les fonctions globales permettent à des variables de passer outre différent dossiers ou de leurs position dans une fonction. Ce programme n'étant composé que de fonction, 'global' sera beaucoup utilisé
    global menubar
    for child in fenetre.winfo_children():          ##On détruit tous le contenu de la page, sauf le menu permettant de passer d'une section à une autre
        if child != menubar:
            child.destroy()

def removeclign_delai():            ##Fonction utilisée plus tard pour permettre la destruction de certaines 'spinbox'
    global Frame_delai              ##global est ici aussi utilisé pour permettre à des 'frame' de se trouver dans plusieurs fonctions
    global Frame_clign
    for child in Frame_clign.winfo_children():          ##Les 'spinbox' se trouver dans des 'frame' définies sont détruites
        child.destroy()
    for child in Frame_delai.winfo_children():
        child.destroy()


def envoyer_date(anne, mois, jour):
    showwarning('changer date')

def envoyer_heure(heure, minute, seconde):
    showwarning('Envoyer l''heure')

def envoyer_message_ecran(message, couleur):
    showwarning('envoyer message')
def envoyer_message_afficheur(message, couleur, clignotement, decalage):
    showwarning('envoyer message')



def changer_date():         ##Cette fonction correspond à la section changer la date, On y retrouves des 'spinbox' pour modifier le jour, le mois, ou l'année
    global fenetre
    removecontent()         ##avant de faire apparaître la section, on détruit tout le contenu de la page sauf le menu

    Frame_chdate = Frame(fenetre)
    Frame_chdate.pack(pady=5, padx=20)

    Frame_jour = Frame(Frame_chdate, width=45, bg="grey")
    Frame_jour.pack(pady=5)

    Frame_mois = Frame(Frame_chdate, width=45, bg="grey")
    Frame_mois.pack(pady=5)

    Frame_annee = Frame(Frame_chdate, width=45, bg="grey")
    Frame_annee.pack(pady=5)

    label_jour = Label(Frame_jour, text="Jour", bg="grey")
    label_jour.pack(side=LEFT, padx=30)

    _jour = Spinbox(Frame_jour, from_=0, to=23, width=8)            ##'spinbox' permettant la modification du jour
    _jour.pack(side=RIGHT)

    label_mois = Label(Frame_mois, text="Mois", bg="grey")
    label_mois.pack(side=LEFT, padx=28)

    _mois = Spinbox(Frame_mois, from_=0, to=59, width=8)            ##'spinbox' permettant la modification du mois
    _mois.pack(side=RIGHT)

    label_annee = Label(Frame_annee, text="Année", bg="grey")
    label_annee.pack(side=LEFT, padx=24)

    _annee = Spinbox(Frame_annee, from_=2000, to=3000, width=8)     ##'spinbox' permettant la modification de l'année
    _annee.pack(side=RIGHT)

    bouton=Button(fenetre, pady=6, text="Enregistrer", command= lambda: envoyer_date(int(_annee.get()), int(_mois.get()), int(_jour.get())))
    bouton.pack()           ##Bouton servant à enregistrer les paramètres de date entrés auparavant

def changer_heure():            ##Cette fonction correspond à la section changer l'heure, On y retrouves des 'spinbox' pour modifier l'heure, les minutes ou les secondes

    global fenetre
    removecontent()             ##avant de faire apparaître la section, on détruit tout le contenu de la page sauf le menu


    Frame_chheure = Frame(fenetre)
    Frame_chheure.pack(pady=5, padx=20)

    Frame_heure = Frame(Frame_chheure, width=45, bg="grey")
    Frame_heure.pack(pady=5)

    Frame_min = Frame(Frame_chheure, width=45, bg="grey")
    Frame_min.pack(pady=5)

    Frame_sec = Frame(Frame_chheure, width=45, bg="grey")
    Frame_sec.pack(pady=5)

    label_heure = Label(Frame_heure, text="Heures", bg="grey")
    label_heure.pack(side=LEFT, padx=22)

    _heure = Spinbox(Frame_heure, from_=0, to=23, width=8)          ##'spinbox' permettant la modification de l'heure
    _heure.pack(side=RIGHT)

    label_min = Label(Frame_min, text="Minutes", bg="grey")
    label_min.pack(side=LEFT, padx=19)

    _min = Spinbox(Frame_min, from_=0, to=59, width=8)          ##'spinbox' permettant la modification des minutes
    _min.pack(side=RIGHT)

    label_sec = Label(Frame_sec, text="Secondes", bg="grey")
    label_sec.pack(side=LEFT, padx=15)

    _sec = Spinbox(Frame_sec, from_=0, to=59, width=8)          ##'spinbox' permettant la modification des secondes
    _sec.pack(side=RIGHT)

    bouton=Button(fenetre, pady=6, text="Enregistrer", command= lambda: envoyer_heure(int(_heure.get()), int(_min.get()), int(_sec.get())))
    bouton.pack()           ##Bouton servant à enregistrer les paramètres d'heure entrés auparavant

def clign_spinbox_fct():            ##Fonction qui fait que, lorsque la 'checkbutton' du clignotement est cochée, une 'spinbox' apparaît, et est détruite lorsque décochée
    global fenetre
    global cpt_clign
    global Frame_clign
    cpt_clign += 1

    if (cpt_clign %2 == 0):         ##Si le reste de la division par deux de compteur est zéro, alors le compteur est paire, donc le checkbutton est décochée, et la spinbox présente dans 'Frame-clign' est détruite
        removeclign_delai()
    else:                           ##Si le reste de la division par deux est autre que zéro (ne peut-être alors que un), alors le compteur est impaire, donc le checbutton est cochée, et la spinbox 'clign_spinbox' apparaît dans 'Frame_clign'
        clign_spinbox = Spinbox(Frame_clign, from_=0.5, to=60)
        clign_spinbox.pack()

def delai_spinbox_fct():            ##Même principe que la fonction précédente, mais avec la spinbox 'delai_spinbox' et la frame 'Frame_delai'
    global fenetre
    global cpt_delai
    global Frame_delai
    cpt_delai += 1

    if (cpt_delai %2 == 0):
        removeclign_delai()
    else:
        delai_spinbox = Spinbox(Frame_delai, from_=5, to=120)
        delai_spinbox.pack()



def changer_message_afficheur():            ##Fonction permettant l'apparition de la section changer le message de l'afficheur
    global fenetre                          ##On appel différente variables d'autres fonctions
    global Frame_clign
    global Frame_delai
    removecontent()                         ##On détruit le contenu déjà présent sur la page, sauf le menu

    entree_afficheur = Entry(fenetre, width=30)         ##champs où pourra être écrit le message à afficher
    entree_afficheur.pack(pady=8, padx=10)

    liste_afficheur = Listbox(fenetre, height=4)        ##liste des différentes couleurs de message disponibles
    liste_afficheur.insert(1, "Noir")
    liste_afficheur.insert(2, "Rouge")
    liste_afficheur.insert(3, "Vert")
    liste_afficheur.insert(4, "Bleu")
    liste_afficheur.pack(pady=3)


    check_clign = Checkbutton(fenetre, text="Clignotement", command=clign_spinbox_fct)          ##checkbutton faisant apparaître une spinbox ou sera rentré une délai entre chaques clignotement
    check_clign.pack()

    Frame_clign = Frame(fenetre, height=19)
    Frame_clign.pack(pady=5)

    check_delai = Checkbutton(fenetre, text="Décalage         ", command=delai_spinbox_fct) ##Ces espaces servent à aligner les deux Checkbutton (dans un but purement esthétique) #checkbutton faisant apparaître une spinbox ou sera rentré une délai entre chaques passage du message
    check_delai.pack()

    Frame_delai = Frame(fenetre, height=19)
    Frame_delai.pack(pady=5)


    bouton=Button(fenetre, pady=6, text="Enregistrer", command= lambda: envoyer_message_afficheur(phrase.get(), liste.get(), Frame_clign.get(), Frame_delai.get()))          #Bouton permettant d'enregistré les changements voulus
    bouton.pack()

def changer_message_ecran():            ##Fonction permettant l'apparition de la section changer le message de l'écran, même fonction que celle ci-dessus mais noms de variables différents et 'délei' et 'clignotement' absents

    global fenetre
    removecontent()

    entree_ecran = Entry(fenetre, width=30)
    entree_ecran.pack(pady=8, padx=10)

    liste_ecran = Listbox(fenetre, height=4)
    liste_ecran.insert(1, "Noir")
    liste_ecran.insert(2, "Rouge")
    liste_ecran.insert(3, "Vert")
    liste_ecran.insert(4, "Bleu")
    liste_ecran.pack(pady=3)


    bouton=Button(fenetre, pady=6, text="Enregistrer", command= lambda: envoyer_message_ecran(phrase.get(),liste.get()))
    bouton.pack()

def load_dashboardwindows(window):          ##Fonction appellée suite à la validation du mot de passe. Comprend a page en elle-même et le menu permettant la navigation entre les différentes sections

    global menubar
    global fenetre
    global socket
    ##socket.connect(('localhost', 12800))

    fenetre = window

    removecontent()             ##On garde la même page que le mot de passe mais on en enlève le contenu
    fenetre.title('Horloge')            ##On en change le nom par 'Horloge'
    menubar = Menu(fenetre)

    menu1 = Menu(menubar, tearoff=0)            ##On créer la barre de menu, et tout son contenu
    menu1.add_command(label="Changer la date", command=changer_date)
    menu1.add_command(label="Changer l'heure", command=changer_heure)

    menubar.add_cascade(label="Parametres", menu=menu1)

    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="Afficheur", command=changer_message_afficheur)
    menu2.add_command(label="Ecran", command=changer_message_ecran)

    menubar.add_cascade(label="Afficher", menu=menu2)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="Fermer la fenêtre", command=fenetre.quit)
    menubar.add_cascade(label="Quitter", menu=menu3)
    fenetre.config(menu=menubar)