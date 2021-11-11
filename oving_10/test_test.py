# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 12:49:21 2021

@author: Andreas
"""

import unittest
from Opp_d import Sporsmål
        
class TestSvar(unittest.TestCase):
    def test_sjekk_svar(self):
        spm1 = Sporsmål("hva er hovedstaden i Norge?", ["Oslo", "Stockholm", "København"], 0)
        spm2 = Sporsmål("Hvilken farge er en banan?", ["Rød", "Gul", "Rød"], 1)
        spm3 = Sporsmål("Hvor mange bokstaver er det i (PC)?", ["1", "5", "2"], 2)
        self.assertEquals(spm1.korrekt, 0)
        self.assertEquals(spm2.korrekt, 1)
        self.assertTrue(spm3.sjekk_svar(2))
        
    def test_korrekt_svar_tekst2(self):
        spm1 = Sporsmål("hva er hovedstaden i Norge?", ["Oslo", "Stockholm", "København"], 0)
        spm2 = Sporsmål("Hvilken farge er en banan?", ["Rød", "Gul", "Rød"], 1)
        spm3 = Sporsmål("Hvor mange bokstaver er det i (PC)?", ["1", "5", "2"], 2)
        self.assertEquals(spm1.Svar_alternativ[0], "Oslo")
        self.assertEquals(spm2.Svar_alternativ[1], "Gul")
        self.assertEquals(spm3.Svar_alternativ[2], "2")
    
if __name__ == "__main__":
    unittest.main()
    
