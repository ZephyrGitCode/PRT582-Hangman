# Importing required libraries
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

# Create the three following golbal variables
word = generateword()
wordlist = listword(word)
hiddenword = hideword(word)

# Reveal word in console, use for testing code
print("Random word: " + word)

# Main tkinter application
class Applicatiion(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # Create all local variables
        self.hiddenword = tk.StringVar()
        self.hiddenword.set(hiddenword)
        self.rightlist = []
        self.wronglist = []
        self.wrongguesses = tk.StringVar()
        self.lives = 6
        self.lifecount = tk.StringVar()
        self.lifecount.set("Lives: "+str(self.lives))
        self.errortext = tk.StringVar()
        # Create each piece of the game window
        self.pack()
        self.create_info()
        self.create_word()
        self.create_lives()
        self.create_entry()
        self.create_guesses()

    # Create the game infomation
    def create_info(self):
        self.gametext = """The objective of Hangman is simply to find the missing word. You have 6 lives which are reduced for each wrong letter guessed. Start guessing!"""
        self.infolabel = tk.Label(self, text=self.gametext, wraplength=250)
        self.infolabel.pack()

    # Create the hidden word
    def create_word(self):
        # textvariable for self.hiddenword allows it to be dynamically updated
        self.wordlabel = tk.Label(self, textvariable=self.hiddenword)
        self.wordlabel.pack()
    
    # Create the life counter
    def create_lives(self):
        self.liveslabel = tk.Label(self, textvariable=self.lifecount)
        self.liveslabel.pack()
    
    # Create the wrong guesses list
    def create_guesses(self):
        self.errorlabel = tk.Label(self, textvariable=self.wrongguesses)
        self.errorlabel.pack()
    
    # Create the input field, error text and confirm button
    def create_entry(self):
        self.entrylabel = tk.Label(self, text="Enter a letter")
        self.entrylabel.pack(side="top")

        self.entry = tk.Entry(self, bd=5)
        self.entry.pack()

        self.errorlabel = tk.Label(self, textvariable=self.errortext)
        self.errorlabel.pack()

        # Button that calls get_entry() function when clicked
        self.entry_btn = tk.Button(self, text="Confirm letter", command=self.get_entry)
        self.entry_btn.pack(side="bottom")
    
    # called by confirm button
    def get_entry(self):
        self.errortext.set("")
        # Checks if entered letter exists and is a letter
        if self.entry.get() and self.entry.get().isalpha():
            self.letter = self.entry.get()[0].upper()
            # Checks if letter is not already in both right and wrong list
            if self.letter not in self.rightlist and self.letter not in self.wronglist:
                if self.letter in word:
                     # If letter in word, append to right list
                    self.rightlist.append(self.letter)
                    # Calls the function to update the hidden word
                    self.updatehidden()
                else:
                    # Calls the function to add wrong letters to screen and reduce a life
                    self.wrongguess()
            else:
                self.errortext.set("You have already guessed this letter")
        else:
            self.errortext.set("Please enter a letter")
        # Clears previous text in entry
        self.entry.delete(0, 'end')

    # Function to reveal letters in hidden word
    def updatehidden(self):
        self.revealedword = self.hiddenword.get()
        # converts current hidden word from string to list
        self.revealedwordlist = []
        for letter in self.revealedword:
            self.revealedwordlist.append(letter)
        # if current letter matches self.letter then reveal the letter
        for letter in range(len(word)):
            if self.letter == word[letter]:
                self.revealedwordlist[letter] = self.letter
        # converts the now revealed list back to string
        self.revealedword = ""
        for letter in self.revealedwordlist:
            self.revealedword+=letter
        # updates the word on display, revealing more letters
        self.hiddenword.set(self.revealedword)
        # Checks if no missing letters, if yes player wins!
        if "_" not in self.revealedword:
            self.hiddenword.set(self.revealedword + " Congratulations, you win!")

    # Function to update wrong letters on display and reduce life count
    def wrongguess(self):
        self.wronglist.append(self.letter)
        self.wrongstring = "Wrong Guesses: "
        # Adds each wrong letter to the list
        for i in range(len(self.wronglist)):
            self.wrongstring += self.wronglist[i]
            self.wrongstring += " "
        # Updates textvariable with new wrong letters list
        self.wrongguesses.set(self.wrongstring)
        # Removes a life from count
        self.lives -= 1
        self.lifecount.set("Lives: "+str(self.lives))
        # If life count is 0 then say defeat and show word
        if self.lives == 0:
            self.hiddenword.set("Defeat Word was: "+word)
        

# Launchs game window
root = tk.Tk()
root.title("Hangman Zephyr")
root.geometry("300x225")
app = Applicatiion(master=root)
app.mainloop()