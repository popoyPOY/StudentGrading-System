from this import d
from tkinter import *
from tkinter import font

from tkinter.ttk import Style
from tkinter.ttk import Treeview


from app import Student
from tkinter import messagebox
import sqlite3

class studenGUI(Tk):
    def __init__(self):
        super().__init__()

        self.style = Style()
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

    # opening the Grade Calculator
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
        window.geometry("1600x1000")

        window.config(bg=self.bgcolor)

        self.guiFrame = Frame(window, bg=self.bgcolor)
        self.guiFrame.pack()

        self.universityLabel = Label(self.guiFrame, text="UNIVERSITY OF DRAGONS", font=("Calibri bold", 20), fg=self.fgcolor, bg=self.bgcolor)
        self.universityLabel.grid(padx=20, pady=20, column=1)

        self.listboxColumn = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        
        #self.style.configure("mystyle.Treeview", font=('Calibri bold', 11))

        self.listbox = Treeview(window, columns=self.listboxColumn, show='headings')
        

        self.listbox.heading('1', text="Student Number")
        self.listbox.heading('2', text="Name")
        self.listbox.heading('3', text="Course")
        self.listbox.heading('4', text="Subject")
        self.listbox.heading('5', text="Prelim")
        self.listbox.heading('6', text="Midterm")
        self.listbox.heading('7', text="Final")
        self.listbox.heading('8', text="Average")
        self.listbox.heading('9', text="Remark")
        self.listbox.heading('10', text="PE")

        self.listbox.pack(padx=30, pady=30)

        
        self.entryFrames = Frame(window)
        self.entryFrames.pack()

        studentNolabel = Label(self.entryFrames, text="Student Number")
        studentNolabel.grid(row = 1, column=1, padx=10, pady=10)

        studentNoEntry = Entry(self.entryFrames, width=20)
        studentNoEntry.grid(row=2, column=1, padx=10, pady=10)

        studentNameLabel = Label(self.entryFrames, text="Student Name")
        studentNameLabel.grid(row = 3, column=1, padx=10, pady=10)

        studentnameEntry = Entry(self.entryFrames, width=20)
        studentnameEntry.grid(row=4, column=1, padx=10, pady=10)

        studentCourseLabel = Label(self.entryFrames, text="Student Course")
        studentCourseLabel.grid(row = 5, column=1, padx=10, pady=10)

        studentCourseEntry = Entry(self.entryFrames, width=20)
        studentCourseEntry.grid(row=6, column=1, padx=10, pady=10)

        studentSubjectLabel = Label(self.entryFrames, text="Student Subject")
        studentSubjectLabel.grid(row = 7, column=1, padx=10, pady=10)

        studentSubjectEntry = Entry(self.entryFrames, width=20)
        studentSubjectEntry.grid(row=8, column=1, padx=10, pady=10)

        studentPrelimLabel = Label(self.entryFrames, text="Student Prelim")
        studentPrelimLabel.grid(row = 9, column=1, padx=10, pady=10)

        studentPrelimEntry = Entry(self.entryFrames, width=20)
        studentPrelimEntry.grid(row=10, column=1, padx=10, pady=10)


        #colum 2
        studentMidtermlabel = Label(self.entryFrames, text="Student MidTerm")
        studentMidtermlabel.grid(row = 1, column=2, padx=10, pady=10)

        studentPrelimEntry = Entry(self.entryFrames, width=20)
        studentPrelimEntry.grid(row=2, column=2, padx=10, pady=10)

        studentFinallabel = Label(self.entryFrames, text="Student Final")
        studentFinallabel.grid(row = 3, column=2, padx=10, pady=10)

        studentFinalEntry = Entry(self.entryFrames, width=20)
        studentFinalEntry.grid(row=4, column=2, padx=10, pady=10)

        studentAveragelabel = Label(self.entryFrames, text="Student Average")
        studentAveragelabel.grid(row = 5, column=2, padx=10, pady=10)

        studentAverageEntry = Entry(self.entryFrames, width=20)
        studentAverageEntry.grid(row=6, column=2, padx=10, pady=10)

        studentRemarklabel = Label(self.entryFrames, text="Student Remark")
        studentRemarklabel.grid(row = 7, column=2, padx=10, pady=10)

        studentRemarkEntry = Entry(self.entryFrames, width=20)
        studentRemarkEntry.grid(row=8, column=2, padx=10, pady=10)

        studentpoinEquivalentLabel = Label(self.entryFrames, text="Student Remark")
        studentpoinEquivalentLabel.grid(row = 9, column=2, padx=10, pady=10)

        studentpoinEquivalentEntry = Entry(self.entryFrames, width=20)
        studentpoinEquivalentEntry.grid(row=10, column=2, padx=10, pady=10)


        

        

        
    
if __name__ == "__main__":
    app = studenGUI()
    app.mainloop()