import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)                      #registre à décalage
GPIO.setup(5, GPIO.OUT, initial=GPIO.HIGH)   #reset du registre si LOW

cpt=0


cpt+=1
if cpt==60:
    GPIO.output(5, 0)
    GPIO.input(5, 1)

else:
    GPIO.output(4, 1)
time.sleep(1)



