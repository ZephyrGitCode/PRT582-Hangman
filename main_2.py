# Importing  required libraries
import tkinter as tk
from english_words import english_words_set

# Generates the random word
def generateword():
    randword = list(english_words_set)[1].upper()
    spacedword = ""
    for letter in randword:
        spacedword += letter
        spacedword += " "
    return spacedword

# Generates a hidden list based on word
def listword(word):
    wordlist = []
    for letter in word:
        if letter != " ":
            wordlist.append("_")
        else:
            wordlist.append(letter)
    return wordlist

# Generates a hidden string based on word
def hideword(word):
    hiddenword = ""
    for letter in word:
        if letter != " ":
            hiddenword += "_"
        else:
            hiddenword += letter
    return hiddenword

word = generateword()
wordlist = listword(word)
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
        self.rightlist = []
        self.revealedword = ""

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
            if self.letter in word and self.letter not in self.rightlist:
                self.rightlist.append(self.letter)
                self.revealedword = self.hiddenword.get()
                # convert string to list
                self.revealedwordlist = []
                for letter in self.revealedword:
                    self.revealedwordlist.append(letter)
                # if current letter matches self.letter then reveal the letter
                for letter in range(len(word)):
                    if self.letter == word[letter]:
                        self.revealedwordlist[letter] = self.letter
                # converts list back to string
                self.revealedword = ""
                for letter in self.revealedwordlist:
                    self.revealedword+=letter
                # re-prints the revealed word to display
                self.hiddenword.set(self.revealedword)
        else:
            self.guess.set("You must enter a letter")
        self.entry.delete(0, 'end')

# Launch game window
root = tk.Tk()
root.title("Hangman Zephyr")
root.geometry("300x225")
app = Applicatiion(master=root)
app.mainloop()