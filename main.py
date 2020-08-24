# Importing  required libraries
import tkinter as tk
from english_words import english_words_set

# Generates random word
word = list(english_words_set)[1]
word = word.upper()
hiddenword = ""
for letter in word:
    hiddenword += "_"

print("Random word: " + word)
print("Random word hidden: " + hiddenword)


# Main tkinter application
class Applicatiion(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.letter = tk.StringVar()
        self.lifecount = tk.StringVar()
        self.lifecount = "6"
        self.hiddenword = tk.StringVar()
        self.hiddenword.set(hiddenword)
        self.rightlist = []
        self.wronglist = []
        self.revealedword = ""

        self.pack()
        self.create_info()
        self.create_word()
        self.create_lives()
        self.create_entry()
    
    def create_info(self):
        self.gametext = """The objective of Hangman is simply to find the missing word. You have 6 lives which are reduced for each wrong letter guessed. Start guessing!"""
        self.infolabel = tk.Label(self, text=self.gametext, wraplength=250)
        self.infolabel.pack()

    def create_word(self):
        self.wordlabel = tk.Label(self, textvariable=self.hiddenword)
        self.wordlabel.pack()

    def create_lives(self):
        self.liveslabel = tk.Label(self, textvariable=self.lifecount)
        self.liveslabel.pack()

    def create_entry(self):
        self.entrylabel = tk.Label(self, text="Enter a letter")
        self.entrylabel.pack(side="top")

        self.entrytext = ""
        self.entry = tk.Entry(self, text=self.entrytext, bd=5)
        self.entry.pack()

        self.entry_btn = tk.Button(self, text="Confirm letter", command=self.get_entry)
        self.entry_btn.pack(side="bottom")

        #self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        #self.quit.pack(side="left")

    # Retrieves the input from the screen
    def get_entry(self):
        self.input = self.entry.get()
        self.letter = self.input[0]
        if self.letter.isalpha():
            self.letter = self.letter.upper()
            print("Random letter screen = " + self.letter)
            if self.letter not in self.rightlist and self.letter not in self.wronglist:
                if self.letter in word:
                    self.revealedword = ""
                    for letter in word:
                        if self.letter == letter:
                            self.revealedword+=self.letter
                        else:
                            self.revealedword+="_"
                else:
                    self.wronglist.append(self.letter)
                    print(self.wronglist)
                    self.lifecount = "6"
                self.hiddenword.set(self.revealedword)
            self.entry.delete(0, 'end')
            
        

# Launch window
root = tk.Tk()
root.title("Hangman Zephyr")
root.geometry("300x225")
app = Applicatiion(master=root)
app.mainloop()