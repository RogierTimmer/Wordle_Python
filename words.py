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


def chooseWord(nguess,nletters):
    global Nguess, Nletters
    Nguess = nguess
    Nletters = nletters
    wordlist = CSV()
    ChosenRandomWord = random.choice(wordlist)
    return ChosenRandomWord



def buttonClicked(RandomChoosenWord):
    if RoundCounter.counter <= Nletters:
        TypedWord = Interface.WordTyped.get()
        temp = checkUserInput(TypedWord)

        if temp is False:
            return

        correction = correctInput(RandomChoosenWord)
        Rounds = RoundCounter()
        Interface.updateInterface(correction, Rounds)
        if WinState() == True:
            messagebox.showerror("Win","You have won the game! Congratulations")
            exit()

    else:
        messagebox.showerror("Lose", f"Unfortunately you did not guess the correct word. The word was \"{RandomChoosenWord}\"")
        exit()

def checkUserInput(TypedWord):
    input = TypedWord
    if len(input) != Nletters:
        messagebox.showerror("input error", "the word does not contain 5 letters")
        return False
    input = input.lower()
    if not input in CSV():
        messagebox.showerror("input error", "word does not exist")
        return False

    return True

def correctInput(RandomchoosenWord):
    global correction
    input = Interface.WordTyped.get()
    word = RandomchoosenWord
    input = list(input)
    word = list(word)
    correction = [0]*Nletters
    copyWord = word

    #if the letter is in the right spot: 3; in the word but in the wrong place: 2; not in the word:1

    for i in range(len(word)):
        if input[i] == word[i]:
            correction[i] = 'green'
            copyWord[i] = 5 # such that that letter is removed from checking again
        elif input[i] in word:
            for j in range(len(word)):
                if input[i] == copyWord[j]:
                    correction[i] = 'yellow'
                    copyWord[j] = 5 # such that that letter is removed from checking again
                    break
        else:
            correction[i] = 'red'
    return correction

def RoundCounter():
    RoundCounter.counter += 1
    if RoundCounter.counter <= Nletters:
        return True
    else:
        return False
RoundCounter.counter = 0

def WinState():
    global correction
    if correction == ['green']*Nletters:
        return True
    else:
        return False