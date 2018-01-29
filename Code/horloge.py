from tkinter import *
from time import *
from math import *
import socket
## Nos fichiers de fonctions
from screen import *
from component import *

##On initialise
launched = False
temp = "17.5"

##Initialisation de la liaison
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 12800))
socket.listen(5)
socket.setblocking(0)
connexion_avec_client = 0
infos_connexion = 0

##Initialisation des registres à décalage


##On créé la fenêtre et synchronise les leds
Fenetre, Canevas = createHorloge()
init_registres()

def horloge():
    ##fonction tournant en boucle (main)
    global Fenetre
    global Canevas
    global connexion_avec_client
    global infos_connexion
    global launched
    global temp

    ##on récupère l'heure et anime les aiguilles en fonction
    heure = gettime()
    animeAigSec(heure[5])
    animeAigMin(heure[4])
    animeAigHeu(heure[3])
    animeTexHeu(heure, temp)
    ##Registres à décalage
    set_registres(heure[5])
    ##Arrivée de la liaison pour le message
    if connexion_avec_client == 0 and infos_connexion == 0:
        try:
            connexion_avec_client, infos_connexion = socket.accept()
            ##animeMessage()
        except BlockingIOError:
            pass
    ##Lecture de l'heure toutes les 10secondes
    if heure[5] % 10 == 0:
        temp = get_temp()

    ##Rappel 100 ms plus tard
    Canevas.after(100, horloge)

##premier appel et loop de la fenetre
horloge()
Fenetre.mainloop()
