from tkinter import *
from time import *
from math import *
## Nos fichiers de fonctions
from ecranHorloge import *

Fenetre, Canevas = createHorloge()

def horloge():
    global Fenetre
    global Canevas

    heure = gettime()
    animeAigSec(heure[5])
    animeAigMin(heure[4])
    animeAigHeu(heure[3])
    animeTexHeu(convertdate(heure))

    Canevas.after(50, horloge)

horloge()
Fenetre.mainloop()

