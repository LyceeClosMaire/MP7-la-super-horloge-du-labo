from tkinter import*
from tkinter.messagebox import *
from ProjetISN_menu import *

def verif_mdp():
    if mdp.get() == '<3':
        for c in fenetre.winfo_children():
            c.destroy()
        load_dashboardwindows(fenetre)
    else:
        showwarning('Résultat','Mot de passe incorrect.')
        motdepasse.set('')

fenetre = Tk()
fenetre.title('Identification requise')

label_mdp = Label(fenetre, text = 'Mot de passe ')
label_mdp.pack(side = LEFT, padx = 5, pady = 5)

mdp= StringVar()
champ = Entry(fenetre, textvariable= mdp, show='*', bg ='WHITE', fg='maroon')
champ.focus_set()
champ.pack(side = LEFT, padx = 5, pady = 5)

bouton = Button(fenetre, text ='Valider', command = verif_mdp)
bouton.pack(side = LEFT, padx = 5, pady = 5)

fenetre.mainloop()
