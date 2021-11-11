# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 09:14:08 2021

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
    def __init__(self, Navn, svar=0, Poengsum=0):
        self.Navn = Navn
        self.Svar = svar
        self.Poengsum = Poengsum
        
def liste_spillere(spillere):
    #Spørre om antall spillere og navn til spillere
    liste_navn_spillere = []
    for spiller in range(spillere):
        navn_spiller = input(f"Skriv inn navn til spiller {spiller}: ")
        liste_navn_spillere.append(Spiller(navn_spiller))
    return liste_navn_spillere
    

if __name__ == '__main__':  
 
    spillere = int(input("Skriv inn antall spillere: "))
    liste_navn = liste_spillere(spillere)
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
        for spiller in liste_navn:
            spiller_svar = int(input(f"{spiller.Navn} skriv inn ditt svar: "))
            spiller.Svar = spiller_svar
        for spiller in liste_navn:
            if spm.sjekk_svar(spiller.Svar):
                spiller.Poengsum += 1
                print(f"{spiller.Navn} Korrekt svar")
            else:
                print(f"{spiller.Navn} Feil svar")
            
        print(spm.korrekt_svar_tekst())
    
    Verdi = 0
    indeks = 0
    for i in range(len(liste_navn)):
        if liste_navn[i].Poengsum > Verdi:
            Verdi = liste_navn[i].Poengsum
            indeks=i
    print(f"{liste_navn[indeks].Navn} har mest poeng: Poengsum: {Verdi}")

   
    

