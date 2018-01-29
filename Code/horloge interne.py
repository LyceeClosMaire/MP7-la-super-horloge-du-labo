from tkinter import *
from time import *
from math import *
import socket
## Nos fichiers de fonctions
from ecranHorloge import *

Fenetre, Canevas = createHorloge()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 12800))
socket.listen(5)
socket.setblocking(0)

connexion_avec_client = 0
infos_connexion = 0

def horloge():
    global Fenetre
    global Canevas
    global connexion_avec_client
    global infos_connexion
    
    
    if connexion_avec_client == 0 and infos_connexion == 0:
        try:
            connexion_avec_client, infos_connexion = socket.accept()
        except BlockingIOError:
            pass        
        
    heure = gettime()
    animeAigSec(heure[5])
    animeAigMin(heure[4])
    animeAigHeu(heure[3])
    animeTexHeu(convertdate(heure))

    Canevas.after(50, horloge)

horloge()
Fenetre.mainloop()

