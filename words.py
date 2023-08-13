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
    print(f"Ik raad aan om {ChosenRandomWord} te raden")    # TODO remove
    input = Interface.ButtonClicked()
    if len(input) != 5:
        print("not enough letters")
        return False
    print("Yes")

    if input in CSV():
        print("good in the list")
    else:
        return False
    return True
