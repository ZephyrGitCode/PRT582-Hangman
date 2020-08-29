# Importing  required libraries
import tkinter as tk
from english_words import english_words_lower_set

def generateword():
    words = list(english_words_lower_set)
    randword = words[1].upper()
    return randword

def hideword(word):
    hiddenword = ""
    for letter in word:
        hiddenword += "_ "
    return hiddenword

word = generateword()
hiddenword = hideword(word)

print("Random word: " + word)
print("Hidden word: " + hiddenword)
# Main tkinter application
class Applicatiion(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.hiddenword = tk.StringVar()
        self.hiddenword.set(hiddenword)
        self.guess = tk.StringVar()

        self.pack()
        self.create_word()
        self.create_entry()

    def create_word(self):
        self.wordlabel = tk.Label(self, textvariable=self.hiddenword)
        self.wordlabel.pack()
    
    def create_entry(self):
        self.entrylabel = tk.Label(self, text="Enter a letter")
        self.entrylabel.pack(side="top")

        self.entry = tk.Entry(self, bd=5)
        self.entry.pack()

        self.guesslabel = tk.Label(self, textvariable = self.guess)
        self.guesslabel.pack()

        self.entry_btn = tk.Button(self, text="Confirm letter", command=self.get_entry)
        self.entry_btn.pack(side="bottom")
        
    def get_entry(self):
        if self.entry.get() and self.entry.get().isalpha():
            self.letter = self.entry.get()[0].upper()
            self.guess.set(self.letter)
        else:
            self.guess.set("You must enter a letter")
        self.entry.delete(0, 'end')

# Launch game window
root = tk.Tk()
root.title("Hangman Zephyr")
root.geometry("300x225")
app = Applicatiion(master=root)
app.mainloop()