import csv
import random

import Interface


def CSV():
    wordlist = []
    with open("valid-words-test.csv") as csvfile:   # TODO have good CVS
        reader = csv.reader(csvfile)
        for row in reader:
            wordlist.append(row[0])
    return wordlist


def chooseWord():
    wordlist = CSV()
    global ChosenRandomWord
    ChosenRandomWord = random.choice(wordlist)
    print(ChosenRandomWord)  # TODO remove



def checkUserInput():
    input = Interface.WordTyped.get()
    print(input)
    if len(input) != 5:
        print("not enough letters")
        return False

    if not input in CSV():
        print("not in list")
        return False

    print("Alle test volstaan")
    return True