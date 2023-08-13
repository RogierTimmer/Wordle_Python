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
    ChosenRandomWord = random.choice(wordlist)
    return ChosenRandomWord


def ButtonClicked(RandomChoosenWord):
    TypedWord = Interface.WordTyped.get()
    msg = f'Your input: {TypedWord}'
    print(RandomChoosenWord,"RandomWord")
    print(msg)
    temp = checkUserInput(TypedWord)

    if temp is False:
        print("Please use a correct word")
        # TODO add a thing to make sure that a new word can be typed

    correctInput(RandomChoosenWord)


def checkUserInput(TypedWord):
    input = TypedWord
    print(input)
    if len(input) != 5:
        print("not enough letters")
        return False

    if not input in CSV():
        print("not in list")
        return False

    print("All test succeeded")
    return True

def correctInput(RandomchoosenWord):
    input = Interface.WordTyped.get()
    Word = RandomchoosenWord
    print(Word)

