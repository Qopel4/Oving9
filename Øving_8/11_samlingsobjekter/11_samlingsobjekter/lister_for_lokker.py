# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 08:39:36 2021

@author: Erlend Tøssebro
"""

liste = [1, 3, 5, 7, 9]

for element in liste:
    element = element*2
    print(element)

print(liste)

element = input("Skriv inn et tall for å sjekke om det er med i lista: ")
element = int(element)
if element in liste:
    print(f"{element} er med i lista")
else:
    print(f"{element} er ikke med i lista")

for indeks, element in enumerate(liste):
    print(f"Element {element} ligger på indeks {indeks}")
