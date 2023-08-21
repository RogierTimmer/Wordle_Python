from tkinter import *
from tkinter import ttk

import words

root = Tk()
WordTyped = StringVar()
frames = []
def interfaceStartup(Nguess,nletters,RandomChoosenword): #Makes the initial interface with the boxes
    global frames, label, Nletters
    Nletters = nletters
    root.title("Wordle")
    for y in range(Nguess):
        word_frames = []
        root.columnconfigure(y, weight=1, minsize=30)
        root.rowconfigure(y, weight=1, minsize=40)
        for x in range(Nletters):
            frame = Frame(root, borderwidth=5, relief="ridge") #Boxes as can be seen in the GUI
            frame.grid(column=x, row=y, sticky=(N, S, E, W))

            label =Label(master=frame, text=" ")                #Needed for the letters in the boxes
            label.pack()
            word_frames.append((frame, label))
        frames.append(word_frames)
    namelbl = ttk.Label(root,text="Guess")
    name = ttk.Entry(root, textvariable=WordTyped)
    root.bind("<Return>", lambda e: (words.buttonClicked(RandomChoosenword)))   #button clicking action
    ok = ttk.Button(root, text="Okay", command=lambda: words.buttonClicked(RandomChoosenword)) #enter clicking action


    root.columnconfigure(5, weight=1)

    namelbl.grid(column=Nletters, row=0, sticky=(N, W), padx=5)
    name.grid(column=Nletters, row=1, sticky=(N,E,W), pady=5, padx=5)
    ok.grid(column=Nletters, row=3)

    root.mainloop()

def updateInterface(correction):        #Updates the interface using the correction made in words.py
    global frames, label, Nletters
    for j in range(Nletters):
        i = words.RoundCounter.counter - 1
        frame, label = frames[i][j]
        frame['background'] = correction[j]
        letters = list(WordTyped.get())
        label.config(text=letters[j])
