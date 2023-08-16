import csv
import random
import numpy
import Interface


def CSV():
    wordlist = []
    with open("valid-words.csv") as csvfile:   # TODO have good CVS
        reader = csv.reader(csvfile)
        for row in reader:
            wordlist.append(row[0])
    return wordlist


def chooseWord():
    print('Choose Word!')
    wordlist = CSV()
    ChosenRandomWord = random.choice(wordlist)
    return ChosenRandomWord


def ButtonClicked(RandomChoosenWord):
    print('Button Clicked!')
    TypedWord = Interface.WordTyped.get()
    msg = f'Your input: {TypedWord}'
    print(RandomChoosenWord,"RandomWord")
    print(msg)
    temp = checkUserInput(TypedWord)

    if temp is False:
        print("Please use a correct word")
        # TODO add a thing to make sure that a new word can be typed
        return

    correctInput(RandomChoosenWord)


def checkUserInput(TypedWord):
    return
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
    word = RandomchoosenWord
    print(word,"is the random word and this is the input word",input)
    input = list(input)
    word = list(word)
    print(len(input)," ",len(word))
    correction = [0,0,0,0,0]
    #numpy.array(correction)    # TODO remove
    copyWord = word

    #if the letter is in the right spot: 3; in the word but in the wrong place: 2; not in the word:1

    for i in range(5):
        print(f"i: {i}")
        if input[i] == word[i]:
            correction[i] = 3
            copyWord[i] = 5
            print(f"Copyword: {copyWord}")
        elif input[i] in word:
            for j in range(5):
                print(f"j: {j}")
                if input[i] == copyWord[j]:
                    correction[i] = 2
                    copyWord[j] = 5 # such that that letter is removed from checking again
                    print(f"Copyword: {copyWord}")
                    print(f"Correction: {correction}")
                    break
                if j == 4:
                    correction[i] = 1
        else:
            correction[i] = 1
    print(correction)
    return correction