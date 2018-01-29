##import sys
import time
##import SDL_DS1307
##import os

def get_temp():
    ##On ouvre pour lecture le fichier temporaire des slaves du bus w1
    f = open('/sys/bus/w1/devices/28-000006d68d51/w1_slave', 'r')
    lines = f.readlines()
    ##On isole la donnée de température qui nous intéresse
    data = lines[1][ lines[1].find('t=') +2:]
    temp = float(data) / 1000.0
    ##ON ferme le fichier et retourne la valeur
    f.closed
    return temp

##filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"
##ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)
##ds1307.write_now()

def get_time():
    ## On récupère l'heure du module tps réel grâce à la bibliothèque
    ##heure = "%s" % ds1307.read_datetime()
    ## On normalise les données

    ##On retourne la valeur
    return heure

def gettime():
    ##get time sans module
    current = time.localtime()
    return current
