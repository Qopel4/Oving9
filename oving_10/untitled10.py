# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:08:05 2021

@author: Andreas
"""

class Sporsmål:
    def __init__(self, spørsmål, Svar_alternativ, korrekt):
        self.spørsmål = spørsmål       
        self.Svar_alternativ = Svar_alternativ
        self.korrekt = korrekt
        
    def __str__(self):
        tekst = self.spørsmål + "\n" 
        for i, alternativ in enumerate(self.Svar_alternativ):
            tekst += f"{i}: {alternativ}\n"
        return tekst
    
    def sjekk_svar(self, Svar):
        if self.korrekt== int(Svar): 
            return True
        else:
            return False
        
    def korrekt_svar_tekst(self): 
        return f"Korekt svar er: {self.Svar_alternativ[self.korrekt]}"
    
    #Brukes i innlevering 10
    def korrekt_svar_tekst2(self):
        return self.Svar_alternativ[self.korrekt]
            
Poengsum = 0
class Spiller: #Egenskapene navn og poengsum
    def __init__(self, Navn, Poengsum):
        self.Navn = Navn
        self.Poengsum = Poengsum
        
def liste_spillere(self):
    #Spørre om antall spillere og navn til spillere
    liste_navn_spillere = []
    for spiller in range(spillere):
        navn_spiller = input(f"Skriv inn navn til spiller {spiller}: ")
        liste_navn_spillere.append(navn_spiller)
    return liste_navn_spillere
    

if __name__ == '__main__':  
 
    spillere = int(input("Skriv inn antall spillere: "))
    #print(liste_spillere(spillere))
    #liste_spillere(spillere) #Lagger en liste med spillere
    
    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as fila:
        liste_spm = []
        for line in fila.readlines():
            lines = line.strip().split(":")
        
            spmtekst = lines[0]
            Svar_alternativ = lines[2].strip(" []\n")
            Svar_alternativ = Svar_alternativ.split(",") 
            for i in range(len(Svar_alternativ)):
                Svar_alternativ[i] = Svar_alternativ[i].strip()
            fasit = int(lines[1])  
            liste_spm.append(Sporsmål(spmtekst, Svar_alternativ, fasit))
       
    for spm in liste_spm:
        print(spm)
        for Svar_spiller in liste_spillere(spillere):
            Svar_spiller = input(f"{Svar_spiller} skriv inn ditt svar: ")
        print(spm.korrekt_svar_tekst())