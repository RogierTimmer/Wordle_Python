# This is a script for wordle using Python

global Nguess, Nletters


Nguess = 6
Nletters = 5

import words
import Interface

roundcount = 0


ChoosenWord = words.chooseWord(Nguess,Nletters)
print(ChoosenWord)

Interface.interfaceStartup(Nguess,Nletters,ChoosenWord)
