# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:17:36 2021

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
    for spiller in range(spillere):
        navn_spiller = input(f"Skriv inn navn til spiller {spiller}: ")
        liste_navn_spillere.append(navn_spiller)
    
        
if __name__ == "__main__":
    spillere = int(input("Skriv inn antall spillere: "))
    liste_spillere(spillere)
    
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
    
    poeng_spiller = 0
    for Poeng_spiller in liste_spillere:
    
    for spm in liste_spm:
        print(spm)
        for Svar_spiller in liste_spillere:
            Svar_spiller = input(f"{Svar_spiller} Skriv inn ditt svar: ")
        print(spm.korrekt_svar_tekst())
        if spm.sjekk_svar(for a in liste_spillere:):
            print(f"{a}: Korrekt svar")
            Poeng_spiller +=1
        
        print(spm.korrekt_svar_tekst() +"\n")
        if spm.sjekk_svar(svar_bruker1):
            print("Bruker1: Korrekt svar")
            Poeng_Bruker1 += 1
        else:
            print("Bruker1: Feil svar")
        if spm.sjekk_svar(svar_bruker2):
            print("Bruker2: Korrekt svar")
            Poeng_Bruker2 += 1
        else:
            print("Bruker2: Feil svar")
    print(f"\nBruker1 fikk {Poeng_Bruker1} poeng.\nBruker2 fikk {Poeng_Bruker2} poeng.\n")
            
            
            
            
            
            
            
            
            
            