# This is a script for wordle using Python
import csv
import random


Nguess = 6
Nletters = 5

import words
import Interface




words.chooseWord()
Interface.interfaceStartup(Nguess,Nletters)
words.checkUserInput()