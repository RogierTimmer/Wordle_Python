from tkinter import *
from tkinter import messagebox

import words


def interfaceOLD():
    root = Tk()

    green = "77b700"
    orange = "fc930a"
    red = "fc930a"

    word = words.userInput()
    words.checkUserInput(word)

    wordInput = Entry(root)
    wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3)

    def Guess():
        global word
        guess = wordInput.get()
        text = Label(root, text=guess).grid(row=0, column=0)

        if not words.checkUserInput(guess):
            messagebox.showerror("kutfeut doe een goed woord!","kutfeut doe een goed woord!")
        return

    wordEnterButton = Button(root, text="Guess", command=Guess)
    wordEnterButton.grid(row=999, column=3, columnspan=2)

    root.mainloop()

    return
