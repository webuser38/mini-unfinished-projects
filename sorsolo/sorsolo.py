import random
import tkinter as tk
from tkinter import filedialog as fd

# Tkinter------------------------------------------------------------------
window = tk.Tk()
window.title("Sorsolás")
window.geometry("450x110") # width x height (x , y)
window.resizable(False, False)
window['bg']='black'

# File reading
#nevek_listaja = []
#with open('nevsor.txt','r') as nevsor:
#    nevsortag = nevsor.readlines()
#    for i in nevsortag:
#        nevsortag_str = i.strip()
#        nevek_listaja.append(nevsortag_str)

#Definitions---------------------------------------------------------------

fileOpened = False
nevek_listaja = []

def fileOpen():
    global filename
    global nevek_listaja
    global fileOpened

    filename = fd.askopenfilename(title='Válassz egy fájlt...', filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    nevek_listaja = []
    with open(filename,'r') as nevsor:
        nevsortag = nevsor.readlines()
        for i in nevsortag:
            nevsortag_str = i.strip()
            nevek_listaja.append(nevsortag_str)
    fileOpened = True

def ujrainditas():
   global fileOpened
   nevek_listaja.clear()
   fileOpened = False
   label.config(text="Sorsolás", font=("",25))

def nevSorsolo():
    if len(nevek_listaja) == 0:
        if fileOpened == True:
            label.config(text="Nincs több ember a névsorban!", font=("",20))
        elif fileOpened == False:
            label.config(text="Előbb tölts be egy fájlt", font=("",25))

    random_nev = random.choice(nevek_listaja)
    label.config(text=random_nev)

    index = nevek_listaja.index(random_nev)
    nevek_listaja.pop(index)


#Window commands-----------------------------------------------------------
label = tk.Label(window, text="Sorsolás", font=("",25), bg="black", fg="green")
label.pack(ipadx = 5, ipady = 5, expand = True)

#kilepes = tk.Button(window, text="X", width = 10, font=("", 10), fg='red', command=lambda: window.quit())
#kilepes.pack(ipadx = 5, ipady = 5, side = tk.LEFT, expand=True)
#kilepes.place(x=0,y=0,width=45, height=45)

ujraindit = tk.Button(window, text="Újraindítás", width = 10, font=("", 10), bg="black", fg="green", command=ujrainditas)
ujraindit.pack(ipadx = 5, ipady = 5, side = tk.LEFT, expand=True)

sorsolas = tk.Button(window, text="Sorsol", width=10, font=("", 10), bg="black", fg="green", command=nevSorsolo)
sorsolas.pack(ipadx = 5, ipady = 5, side = tk.RIGHT, expand=True)

fajlmegnyitas= tk.Button(window, text="Fájl", width = 10, font=("", 10), bg="black", fg="green", command=fileOpen)
fajlmegnyitas.pack(ipadx = 5, ipady = 5, side = tk.RIGHT, expand=True)


#Main loop for the window--------------------------------------------------
window.mainloop()
