from tkinter import *
import words

def interface():
    root = Tk()

    green = "77b700"
    orange = "fc930a"
    red = "fc930a"

    word = words.userInput()
    words.checkUserInput(word)

    wordInput = Entry(root)
    wordInput.grid(row = 999, column = 0, padx = 10, pady =10, columnspan = 3)



    wordEnterButton = Button(root,text="Guess")
    wordEnterButton.grid(row = 999, column = 3, columnspan= 2)


    root.mainloop()

    return
