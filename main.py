# This is a script for wordle using Python
import csv
import random


Nguess = 6
Nletters = 5

import words
import Interface

roundcount = 0


ChoosenWord = words.chooseWord()
print(ChoosenWord)

Interface.interfaceStartup(Nguess,Nletters,ChoosenWord,roundcount)
