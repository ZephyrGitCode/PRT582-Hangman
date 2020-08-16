# Importing  required libraries
import tkinter as tk

# Main tkinter application
class Applicatiion(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create()

    def create(self):
        self.hello = tk.Button(self)
        self.hello["text"] = "Hello World\n(Click me)"
        self.hello["command"] = self.say_hi
        self.hello.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="left")

    def say_hi(self):
        print("Hello0 wworld")

# Launch window
root = tk.Tk()
root.title("Hangman Zephyr")
root.geometry("300x225")
app = Applicatiion(master=root)
app.mainloop()