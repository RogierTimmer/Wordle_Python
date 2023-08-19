from tkinter import *
from tkinter import ttk

import words

root = Tk()
WordTyped = StringVar()
frames = []
def interfaceStartup(Nguess,Nletters,RandomChoosenword,roundcount):
    global frames, label
    root.title("Wordle")
    for y in range(Nguess):
        word_frames = []
        root.columnconfigure(y, weight=1, minsize=30)
        root.rowconfigure(y, weight=1, minsize=40)
        for x in range(Nletters):
            frame = Frame(root, borderwidth=5, relief="ridge")
            frame.grid(column=x, row=y, sticky=(N, S, E, W))

            label =Label(master=frame, text=" ")
            label.pack()
            word_frames.append((frame, label))
        frames.append(word_frames)
    namelbl = ttk.Label(root,text="Guess")
    name = ttk.Entry(root, textvariable=WordTyped)
    root.bind("<Return>", lambda e: (words.ButtonClicked(RandomChoosenword, roundcount)))
    ok = ttk.Button(root, text="Okay", command=lambda: words.ButtonClicked(RandomChoosenword,roundcount))


    root.columnconfigure(5, weight=1)

    namelbl.grid(column=5, row=0, sticky=(N, W), padx=5)
    name.grid(column=5, row=1, sticky=(N,E,W), pady=5, padx=5)
    ok.grid(column=5, row=3)

    root.mainloop()

def updateInterface(correction,round):
    global frames, label
    for j in range(5):
        i = words.RoundCounter.counter - 1
        frame, label = frames[i][j]
        frame['background'] = correction[j]
        letters = list(WordTyped.get())
        label.config(text=letters[j])
