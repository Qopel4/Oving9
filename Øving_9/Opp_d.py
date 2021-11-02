# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:15:35 2021

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
            

if __name__ == '__main__':    
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
            
    Poeng_Bruker1 = 0
    Poeng_Bruker2 = 0
       
    for spm in liste_spm:
        print(spm)
        svar_bruker1 = input("Skriv inn ditt svar: ")
        svar_bruker2 = input("Skriv inn ditt svar: ")
        
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

    
    
  