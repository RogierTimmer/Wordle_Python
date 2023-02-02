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
    chWord = random.choice(wordlist)
    print(chWord)
    return chWord


def userInput():
    guess = input("Choose a word: ")
    return guess


def checkUserInput():
    secret_word = chooseWord()
    print(f"Ik raad aan om {secret_word} te raden")
    guess = userInput()

    if len(guess) != 5:
        print("not enough letters")
        return False
    print("Yes")

    if guess in CSV():
        print("good in the list")
    else:
        return False
    return True
