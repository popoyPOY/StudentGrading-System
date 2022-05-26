from tkinter import *
from app import Student
from tkinter import messagebox
import sqlite3

class studenGUI(Tk):
    def __init__(self):
        super().__init__()

        self.title("Hello World")
        self.geometry("500x500")
        self.config(bg="#354259")
        self.fgcolor = "#C2DED1"
        self.bgcolor = "#354259"

        self.welcomLabel = Label(self, text="UNIVERSITY OF DRAGONS", font=("Arial bold", 20), fg="#F24C4C", bg=self.bgcolor)
        self.welcomLabel.pack(padx=20, pady=20)

        self.loginForm = Frame(self, bg=self.bgcolor)
        self.loginForm.pack()

        self.usernameLabel = Label(self.loginForm, text="Username", font=("Arial bold", 13), bg=self.bgcolor, fg=self.fgcolor)
        self.usernameLabel.grid(row=1)

        self.usernameEntry = Entry(self.loginForm, font=("Calibri bold", 14), bg="#CDC2AE", fg="#293462")
        self.usernameEntry.grid(row=1, column=1, padx=10, pady=10)

        self.usernameLabel = Label(self.loginForm, text="Password", font=("Arial bold", 13), bg=self.bgcolor, fg=self.fgcolor)
        self.usernameLabel.grid(row=2)

        self.passwordEntry = Entry(self.loginForm, font=("Calibri bold", 14), bg="#CDC2AE", fg="#293462", show="*")
        self.passwordEntry.grid(row=2, column=1, padx=10, pady=10)

        self.loginButton = Button(self, text="Login", font=("Calibri bold", 14), width=15,command=self.openGradeCaculator, bg=self.bgcolor, fg=self.fgcolor)
        self.loginButton.pack(padx=10, pady=10)

    def openGradeCaculator(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        login = Student.loginAccount(username=username, password=password)
        
        if login:
            self.gradeCaculator()
            self.withdraw()
    

    #Student Database
    def gradeCaculator(self):
        window = Toplevel()
        window.geometry("1500x1000")


        self.guiFrame = Frame(window)
        self.guiFrame.pack()


        

        

        
    
if __name__ == "__main__":
    app = studenGUI()
    app.mainloop()