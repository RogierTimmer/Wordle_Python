import csv
import random


def CSV():
    wordlist = []
    with open("valid-words.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            wordlist.append(row[0])
    return wordlist


def chooseWord():
    wordlist = CSV()
    global chWord
    chWord = random.choice(wordlist)
    print(chWord)


def userInput():
    guess = input("Choose a word: ")
    return guess


def checkUserInput(input):

    print(f"Ik raad aan om {chWord} te raden")

    if len(input) != 5:
        print("not enough letters")
        return False
    print("Yes")

    if input in CSV():
        print("good in the list")
    else:
        return False
    return True
