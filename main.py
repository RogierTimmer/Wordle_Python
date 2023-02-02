# This is a script for wordle using Python
import csv
import random

Nwords = 5


def CSV():
    wordlist = []
    with open("valid-words.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            wordlist.append(row)
    return wordlist


def chooseWord():
    wordlist = CSV()
    listLength = len(wordlist)
    chWord = random.choice(wordlist)
    print(chWord)
    return chWord

def userInput():
    guess = input("Choose a word: ")
    return guess


def checkUserInput():
    guess = userInput()

    if len(guess) != 5:
        print("not enough")
        return False
    print("Yes")

checkUserInput()