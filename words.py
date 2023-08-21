import csv
import random
from tkinter import messagebox
import Interface



def CSV():      #reads the csv file
    wordlist = []
    with open("5_letter_words.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            wordlist.append(row[0])
    return wordlist


def chooseWord(nguess,nletters):    #chooses a random word
    global Nguess, Nletters
    Nguess = nguess
    Nletters = nletters
    wordlist = CSV()
    ChosenRandomWord = random.choice(wordlist)
    return ChosenRandomWord



def buttonClicked(RandomChoosenWord):       #logic when the button is clicked
    if RoundCounter.counter <= Nletters:
        TypedWord = Interface.WordTyped.get()
        temp = checkUserInput(TypedWord)

        if temp is False:
            return

        correction = correctInput(RandomChoosenWord)
        Rounds = RoundCounter()
        Interface.updateInterface(correction)
        if WinState() == True:
            messagebox.showerror("Win","You have won the game! Congratulations")
            exit()

    else:
        messagebox.showerror("Lose", f"Unfortunately you did not guess the correct word. The word was \"{RandomChoosenWord}\"")
        exit()

def checkUserInput(TypedWord):  #checkes user input if valid
    input = TypedWord
    if len(input) != Nletters:
        messagebox.showerror("input error", "the word does not contain 5 letters")
        return False
    input = input.lower()
    if not input in CSV():
        messagebox.showerror("input error", "word does not exist")
        return False

    return True

def correctInput(RandomchoosenWord):    #corrects the user input
    global correction
    input = Interface.WordTyped.get()
    word = RandomchoosenWord
    input = list(input)
    word = list(word)
    correction = [0]*Nletters
    copyWord = word

    #if the letter is in the right spot: 'green'; in the word but in the wrong place: 'yellow'; not in the word: 'red'

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

def RoundCounter(): #counts the rounds and knows when the rounds are over
    RoundCounter.counter += 1
    if RoundCounter.counter <= Nletters:
        return True
    else:
        return False
RoundCounter.counter = 0

def WinState():     #looks if the user won the game
    global correction
    if correction == ['green']*Nletters:
        return True
    else:
        return False