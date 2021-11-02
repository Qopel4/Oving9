# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:33:48 2021

@author: Erlend Tøssebro
"""

# Lager ei tom liste
liste = list()

# Lager ei liste med oppgitte elementer, her tallene 1, 2, 3, 4 og 5
liste2 = [1, 2, 3, 4, 5]

# Skriver ut lengden til lista
print(len(liste2))

# Legger til elementet 4 i lista "liste"
liste.append(4)

# Legger til elementet 7 i lista "liste2"
liste2.append(7)

# Henter it elementet med indeks 3 og skriver det ut. Merk
# at Python teller fra 0, første elemenet i lista har indeks 0!
print(liste2[3])

# Elementene i ei liste kan være hva som helst
liste.append("En streng")

# Inkludert andre lister
liste.append([9, 8, 7])

# Kan oversrive verdien på en bestemt indeks med tilordning
liste2[2] = 9

# Negative indekser teller fra slutten
print(liste2[-1])

# Setter inn elementet 10 på indeks 2. Dette forskyver
# alle elementer som er etterpå en plass lengre ut i lista
liste2.insert(2, 10)

# For lister inni lister, bruk flere indekser etter herandre.
# For eksempel denne, som kan leses
# Hent ut elementet med indeks 2 i liste. Hent ut elementet
# med indeks 1 i lista som ligger i indeks 2 i liste.
print(liste[2][1])

# Lager ei liste hvor innholdet er lik indeksene
liste_indekser = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Lager ei ny liste so består av elementene fra og med
# indeks 3, til men ikke med indeks 8, i liste_indekser
test = liste_indekser[3:8]
print(test)

# Starter fra starten av lista og går til men ikke med indeks 8
print(liste_indekser[:8])

# Starter på indeks 8 og går til slutten av lista
print(liste_indekser[8:])

# Starter på indeks 1 og tar med bare nnenhvert element.
# Stopper rett før den når indeks 10
print(liste_indekser[1:10:2])

# Finner det minste elementet
print(min(liste_indekser))

# Finner det største elementet
print(max(liste_indekser))

liste3 = [1, 2, 3, 4, 5]
liste4 = [9, 10, 11, 12]

# Kan bruke + operatoren til å slå sammen lister
liste5 = liste3 + liste4

# Kan bruke * operatoren til å repetere ei liste. Denne lager
# ei liste med elementene 0,1 repetert 5 ganger
liste6 = [0, 1]*5

# Skriver ut første indeks som inneholder elementet 10
print(liste4.index(10))

# Fjerner første forekomst av elementet 9 fra lista
liste5.remove(9)

# Fjerner elementet som ligger på indeks 5 fra lista
del liste5[5]

# Sorterer lista. Denne modifiserer lista slik at den er sortert
liste5.sort()

# Reverserer lista slik at den får motsatt rekkefølge
liste2.reverse()
