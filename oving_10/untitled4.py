# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 09:10:58 2021

@author: Andreas
"""
    
Poengsum = 0
class Spiller: #Egenskapene navn og poengsum
    def __init__(self, Navn, Poengsum):
        self.Navn = Navn
        self.Poengsum = Poengsum
        
     
def liste_spillere(self):
    #Spørre om antall spillere og navn til spillere
    liste_navn_spillere = []
    spillere = int(input("Skriv inn antall spillere: "))
    for spiller in range(spillere):
        navn_spiller = input(f"Skriv inn navn til spiller {spiller}: ")
        liste_navn_spillere.append(navn_spiller)
    
        
if __name__ == "__main__":
    spillere = int(input("Skriv inn antall spillere: "))
    liste_spillere(spillere)



    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        