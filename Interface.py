from tkinter import *
from tkinter import ttk

root = Tk()
WordTyped = StringVar()

def interfaceStartup(Nguess,Nletters):

    root.title("Wordle")
    for y in range(Nguess):
        root.columnconfigure(y, weight=1, minsize=30)
        root.rowconfigure(y, weight=1, minsize=40)
        for x in range(Nletters):
            frame = ttk.Frame(root, borderwidth=5, relief="ridge")
            frame.grid(column=x, row=y, sticky=(N, S, E, W))

    namelbl = ttk.Label(root,text="Guess")
    name = ttk.Entry(root, textvariable=WordTyped)
    ok = ttk.Button(root, text="Okay", command=ButtonClicked)

    ok.bind()

    root.columnconfigure(5, weight=1)

    namelbl.grid(column=5, row=0, sticky=(N, W), padx=5)
    name.grid(column=5, row=1, sticky=(N,E,W), pady=5, padx=5)
    ok.grid(column=5, row=3)

    root.mainloop()

def ButtonClicked():
    msg = f'Your input: {WordTyped.get()}'
    print(msg)
    return WordTyped.get