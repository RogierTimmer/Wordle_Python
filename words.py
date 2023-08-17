import csv
import random
from tkinter import messagebox

import Interface

def CSV():
    wordlist = []
    with open("valid-words.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            wordlist.append(row[0])
    return wordlist


def chooseWord():
    print('Choose Word!')
    wordlist = CSV()
    ChosenRandomWord = random.choice(wordlist)
    return ChosenRandomWord



def ButtonClicked(RandomChoosenWord, roundcount):
    print('Button Clicked!')
    TypedWord = Interface.WordTyped.get()
    msg = f'Your input: {TypedWord}'
    print(RandomChoosenWord,"RandomWord")
    print(msg)
    temp = checkUserInput(TypedWord)

    if temp is False:
        print("Please use a correct word")
        return

    correctInput(RandomChoosenWord)
    Rounds = RoundCounter()
    print(f"RoundCounter.counter = {RoundCounter.counter}")
    print(f"Can we go another round: {Rounds}")


def checkUserInput(TypedWord):
    input = TypedWord
    print(input)
    if len(input) != 5:
        messagebox.showerror("input error", "the word does not contain 5 letters")
        return False
    input = input.lower()
    if not input in CSV():
        messagebox.showerror("input error", "word does not exist")
        return False

    print("All test succeeded")
    return True

def correctInput(RandomchoosenWord):
    input = Interface.WordTyped.get()
    word = RandomchoosenWord
    print(word,"is the random word and this is the input word",input)
    input = list(input)
    word = list(word)
    correction = [0,0,0,0,0]
    copyWord = word

    #if the letter is in the right spot: 3; in the word but in the wrong place: 2; not in the word:1

    for i in range(5):
        if input[i] == word[i]:
            correction[i] = 3
            copyWord[i] = 5
        elif input[i] in word:
            for j in range(5):
                if input[i] == copyWord[j]:
                    correction[i] = 2
                    copyWord[j] = 5 # such that that letter is removed from checking again
                    break
                if j == 4:
                    correction[i] = 1
        else:
            correction[i] = 1
    return correction

def RoundCounter():
    RoundCounter.counter += 1
    if RoundCounter.counter <= 5:
        return True
    else:
        return False
RoundCounter.counter = 0