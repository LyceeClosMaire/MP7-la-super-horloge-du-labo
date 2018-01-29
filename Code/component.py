##import sys
import time
import RPi.GPIO as GPIO
import SDL_DS1307
##import os
hour = 0

def get_temp():
    ##On ouvre pour lecture le fichier temporaire des slaves du bus w1
    f = open('/sys/bus/w1/devices/28-000006d68d51/w1_slave', 'r')
    lines = f.readlines()
    ##On isole la donnÃƒÂ©e de tempÃƒÂ©rature qui nous intÃƒÂ©resse
    data = lines[1][ lines[1].find('t=') +2:]
    temp = float(data) / 1000.0
    ##ON ferme le fichier et retourne la valeur
    f.closed
    return temp

##filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"
##ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)
##ds1307.write_now()

def get_time():
    ## On rÃƒÂ©cupÃƒÂ¨re l'heure du module tps rÃƒÂ©el grÃƒÂ¢ce ÃƒÂ  la bibliothÃƒÂ¨que
    ##heure = "%s" % ds1307.read_datetime()
    ## On normalise les donnÃƒÂ©es

    ##On retourne la valeur
    return heure

def gettime():
    ##get time sans module
    current = time.localtime()
    return current

def init_registres():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT, initial=GPIO.HIGH)

def set_registres(heure):
    global hour
    ##Si les secondes = 0, remettre à 0
    if heure == 0:
        hour = 0
        GPIO.output(5, 0)
        GPIO.input(5, 1)
    ##Si changement de seconde, allumer LED supplÃ©mentaire
    elif heure != hour:
        hour = heure[5]
        GPIO.output(4, 0)
        GPIO.output(4, 1)
