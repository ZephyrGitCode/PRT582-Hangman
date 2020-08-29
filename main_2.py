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

        self.pack()
        self.create_word()

    def create_word(self):
        self.wordlabel = tk.Label(self, textvariable=self.hiddenword)
        self.wordlabel.pack()

        #self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        #self.quit.pack(side="left")

    
    """ def get_entry(self):
        letter = self.entry.get()
        print("Random letter screen = " + letter) """

# Launch game window
root = tk.Tk()
root.title("Hangman Zephyr")
root.geometry("300x225")
app = Applicatiion(master=root)
app.mainloop()