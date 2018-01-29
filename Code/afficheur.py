import time
#import serial

def afficher_char(char, pos):
    """Afficher le caractere char a l'addresse pos de l'afficheur en rs232""" 
    data = bytearray.fromhex('FF')
    data = b''.join([data, bytes([pos]), char.encode('ascii')])
    #print(data)
    #ser.write(data)   
    
    print(char, end='')

class Afficheur:
    """Class de l'objet afficheur pour geree l'afficheur"""
    def __init__(self, message, begin, size):
        """Constructeur"""
        self.message = message
        self.begin = begin
        self.size = size
        
        self.decalage = 0
        self.show = True
        
        self.vitesseD = 0
        self.vitesseC = 1
        
        self.lastdecalage = 0
        self.lastclignotement = 0
    
    def setClicnotement(self, vitesse):
        self.vitesseC = vitesse
    
    def setDecalage(self, vitesse):
        self.vitesseD = vitesse
    
    def setMessage(self, message):
        self.message = message
    
    def afficher(self):
        """Affiche sur l'afficheur le message en prennant en compte le decalage"""
        if self.show:
            for i in range(1, self.size + 1):
                afficher_char(self.message[(i - self.decalage) % len(self.message)], self.begin + i - 1)
        else:
            for i in range(0, self.size):
                afficher_char(" ", i)
        print(" ")
    
    def render(self):
        """"Gere le rendu avec le decalage et tout"""
        now = time.time()
        
        if self.vitesseD != 0:
            if self.vitesseD < 0:
                if (now - self.lastdecalage) > -self.vitesseD:
                    self.decalage += 1
                    self.lastdecalage = now
            elif self.vitesseD > 0:
                if (now - self.lastdecalage) > self.vitesseD:
                    self.decalage += 1
                    self.lastdecalage = now
        if self.vitesseC != 0:
            if (now - self.lastclignotement) > self.vitesseC:
                self.show = not self.show
                self.lastclignotement = now
        else:
            self.show = True
            
        self.afficher()