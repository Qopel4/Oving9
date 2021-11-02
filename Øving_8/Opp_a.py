# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 09:38:56 2021

@author: Andreas
"""

#Leser gjennom en tekstfil
#Registrere hvert ord og linjenummeret der det først forekommer
#Skrive ut ordene og linjenumrene

#Åpner tekstfilen 
ordliste = {}
with open("oving_1_rein_tekst.txt", "r", encoding="UTF8") as fila:
    for i,linje in enumerate(fila):
        ordene = linje.strip(".,()").split() 
        for ordet in set(ordene):
            ordliste.setdefault(ordet, []).append(i+1)
for k in sorted(ordliste):
    print(k+":", *ordliste[k])

           
                            
        