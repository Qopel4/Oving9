# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:20:06 2021

@author: Andreas
"""

    #Spørre om antall spillere og navn til spillere
liste_navn_spillere = []
spillere = int(input("Skriv inn antall spillere: "))
for spiller in range(spillere):
    navn_spiller = input(f"Skriv inn navn til spiller {spiller}: ")
    liste_navn_spillere.append(navn_spiller)