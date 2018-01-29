from tkinter import*            ##On importe le module d'objet tkinter
from tkinter.messagebox import *            ##On importe un module de messages d'alerte
from dashboard import *            ##On importe ProjetISN_menu.py dans lequel se trouve la page des paramètres

def verif_mdp():                ##fonction permettant la vérification du mot de passe
    if mdp.get() == 'jules123':           ##On vérifie que le mot de passe est le bon, c'est aussi ici qu'on définit le mot de passe voulut
        load_dashboardwindows(fenetre)          ##Si le mot de passe et bon, on appel la fonction load_dashboardwindows() provenant ProjetISN_menu.py qui permet d'accéder à la page
    else:
        showwarning('Résultat','Mot de passe incorrect.')           ##Si le mot de passe est faux, On prévient l'utilisateur de son erreur par un message provenant de tkinter.messagebox
        motdepasse.set('')


fenetre = Tk()          ##On créer une fenêtre grâce à tkinter, s'appelant fenetre
fenetre.title('Identification requise')         ##Cette fenêtre à pour titre 'Identification requise'

label_mdp = Label(fenetre, text = 'Mot de passe ')          ##On créer une ligne d'écriture 'Mot de passe'
label_mdp.pack(side = LEFT, padx = 5, pady = 5)         ##On donne à cette ligne des propriétés de mise en page

mdp= StringVar()            ##On annonce que ce qui est entré dans le champ d'écriture correspond à la variable 'mdp'
champs = Entry(fenetre, textvariable= mdp, show='*', bg ='WHITE', fg='maroon')           ##On créer ce champs d'écriture
champs.focus_set()           ##On dit que ce champ est initialement vide
champs.pack(side = LEFT, padx = 5, pady = 5)         ##On donne ses propriétés de mise en page au champs

bouton = Button(fenetre, text ='Valider', command = verif_mdp)          ##On creér un bouton permettant d'appeller la foncion verif_mdp()
bouton.pack(side = LEFT, padx = 5, pady = 5)            ##On donne ses propriétés de mise en page au bouton

fenetre.mainloop()          ##On clos le contenu de 'fenetre' et lui demandons de se répeter continuellement
