# Importing  required libraries
import tkinter as tk
from english_words import english_words_lower_set

words = list(english_words_lower_set)
word = words[1]
print("Random word: " + word)

letter = tk.StringVar() 

# Main tkinter application
class Applicatiion(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_items()



    def create_items(self):
        self.entrylabel = tk.Label(self, text="Enter a letter")
        self.entry = tk.Entry(self, bd=5)


        #self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        #self.quit.pack(side="left")

    def say_hi(self):
        print("Hello0 wworld")

    def get_entry(self):
        letter = self.entry.get()
        print("Random letter screen = " + letter)

# Launch window
root = tk.Tk()
root.title("Hangman Zephyr")
root.geometry("300x225")
app = Applicatiion(master=root)
app.mainloop()