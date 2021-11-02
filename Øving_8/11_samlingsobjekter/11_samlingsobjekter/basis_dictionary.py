# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:06:53 2021

@author: Erlend Tøssebro
"""

# Dictionary, map, assosiativ tabell
# Assosierer nøkler med verdier
#  Nøkkel: Det du leiter etter. Må være immutable
#  Verdi: Verdien du finner. Kan være hva som helst
# Hvordan assosiative tabeller ser ut inni er DAT200 pensum

dictionary = dict()
dictionary["Jan Johansen"] = 12345678 # Nøkkel: "Jan Johansen", Verdi: 12345678
dictionary["Berit Nilsen"] = 98765432
dictionary["Hans Henriksen"] = 87654321

dict_konstant = {"Erling Hansen":634523452, "Birgit Ås": 24124214}

for nokkel in dictionary:
    print(nokkel + ": ", end="")
    print(dictionary[nokkel])

