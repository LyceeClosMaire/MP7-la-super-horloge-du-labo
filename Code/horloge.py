from tkinter import *
from time import *
from math import *
import socket
## Nos fichiers de fonctions
from ecran import *
from capteurs import *

##On initialise et créé la fenetre
Fenetre, Canevas = createHorloge()
launched = False
temp = "17.5"

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 12800))
socket.listen(5)
socket.setblocking(0)

connexion_avec_client = 0
infos_connexion = 0

def horloge():
    ##fonction tournant en boucle (main)
    global Fenetre
    global Canevas
<<<<<<< Updated upstream:Code/horloge interne.py
    global connexion_avec_client
    global infos_connexion
    
    
    if connexion_avec_client == 0 and infos_connexion == 0:
        try:
            connexion_avec_client, infos_connexion = socket.accept()
        except BlockingIOError:
            pass        
        
=======
    global launched
    global temp

    ##on récupère l'heure et anime les aiguilles en fonction
>>>>>>> Stashed changes:Code/horloge.py
    heure = gettime()
    animeAigSec(heure[5])
    animeAigMin(heure[4])
    animeAigHeu(heure[3])
    animeTexHeu(heure, temp)
    if heure[5] % 10 == 5 and launched == False:
        launched = True
        animeMessage()
    ##elif heure[5] % 10 == 0:
    ##    temp = get_temp()

    Canevas.after(100, horloge)

##premier appel et loop de la fenetre
horloge()
Fenetre.mainloop()

