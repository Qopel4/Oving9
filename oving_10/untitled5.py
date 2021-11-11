# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 10:03:10 2021

@author: Andreas
"""
    
liste_navn_spillere = []
spillere = int(input("Skriv inn antall spillere: "))
for spiller in range(spillere):
    navn_spiller = input(f"Skriv inn navn til spiller {spiller}: ")
    liste_navn_spillere.append(navn_spiller)
    