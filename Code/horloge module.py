# imports

import sys
import time
import datetime
import SDL_DS1307
from Tkinter import *

# Main Program

filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"
starttime = datetime.datetime.utcnow()

ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)
ds1307.write_now()

currenttime = datetime.datetime.utcnow()
deltatime = currenttime - starttime


def print_hour():
	heure = "%s" % ds1307.read_datetime()
	Label1["text"] = heure
	Label1.after(1000, print_hour)


fenetre = Tk()
Label1 = Label(fenetre, text="Horloge numerique", bg="black", fg="white", width="500", height="200", font="Ubuntu 100")
Label1.pack()

fenetre.after(0, print_hour)
fenetre.mainloop()
