# Importing  required libraries
import tkinter as tk
from english_words import english_words_set

# Generates random word
word = list(english_words_set)[1]
word = word.upper()
spacedword = ""
for letter in word:
    spacedword += letter
    spacedword += " "
word = spacedword

hiddenword = ""
wordlist = []
# Generating list of underscores
for letter in word:
    if letter != " ":
        hiddenword += "_"
        wordlist.append("_")
    else:
        hiddenword += " "
        wordlist.append(" ")

print("Random word: " + word)
print("Random word hidden: " + hiddenword)

# Main tkinter application
class Applicatiion(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.letter = tk.StringVar()
        self.lives = 6
        self.lifecount = tk.StringVar()
        self.lifecount.set(str(self.lives))
        self.hiddenword = tk.StringVar()
        self.hiddenword.set(hiddenword)
        self.rightlist = []
        self.wrongguesses = tk.StringVar()
        self.wronglist = []
        self.revealedword = ""
        

        self.pack()
        self.create_info()
        self.create_word()
        self.create_lives()
        self.create_entry()
        self.create_guesses()
    
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

    def create_guesses(self):
        self.guesslabel = tk.Label(self, textvariable=self.wrongguesses)
        self.guesslabel.pack()

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
                    self.rightlist.append(self.letter)
                    self.revealedword = self.hiddenword.get()
                    self.revealedwordlist = []
                    # convert string to list
                    for letter in self.revealedword:
                        self.revealedwordlist.append(letter)
                    # for i in range(0, length of word) if current letter matches self.letter then reveal the letter
                    for letter in range(len(word)):
                        if word[letter] == self.letter:
                            self.revealedwordlist[letter] = self.letter
                    
                    # converts list back to string
                    self.revealedword = ""
                    for letter in self.revealedwordlist:
                        self.revealedword+=letter
                    # re-prints the revealed word to display
                    self.hiddenword.set(self.revealedword)

                else:
                    # Append letter to wrong guesses list then print them to screen
                    self.wronglist.append(self.letter)
                    self.wrongstring = "Wrong Guesses: "
                    for i in range(len(self.wronglist)):
                        self.wrongstring += self.wronglist[i]
                        self.wrongstring += " "
                    self.wrongguesses.set(self.wrongstring)
                    print(self.wronglist)
                    self.lives -= 1
                    if self.lives == 0:
                        self.hiddenword.set("Defeat")
                        self.lifecount.set("Defeat")
                    self.lifecount.set(str(self.lives))
                
            self.entry.delete(0, 'end')

    """         
    def create_loss(self):
        self.guesslabel = tk.Label(self, textvariable=self.wrongguesses)
        self.guesslabel.pack()
    
    def create_win(self):
        self.guesslabel = tk.Label(self, textvariable=self.wrongguesses)
        self.guesslabel.pack()
    """ 
        

# Launch window
root = tk.Tk()
root.title("Hangman Zephyr")
root.geometry("300x225")
app = Applicatiion(master=root)
app.mainloop()