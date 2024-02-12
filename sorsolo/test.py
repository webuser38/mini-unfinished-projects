import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("Sorsolás")
window.geometry("450x110") # width x height (x , y)
window.resizable(False, False)


def fileOpen():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    print(file_path)



ujraindit = tk.Button(window, text="Fájl", width = 10, font=("", 10), command=lambda: fileOpen())
ujraindit.pack(ipadx = 5, ipady = 5, side = tk.RIGHT, expand=True)


window.mainloop()