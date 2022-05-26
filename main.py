from tkinter import *
from tkinter import font

from tkinter.ttk import Combobox, Style
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
        self.student = Student(0)

        self.welcomLabel = Label(self, text="UNIVERSITY OF DRAGONS", font=("Arial bold", 20), fg="#F24C4C", bg=self.bgcolor)
        self.welcomLabel.pack(padx=20, pady=20)

        self.loginForm = Frame(self, bg=self.bgcolor)
        self.loginForm.pack()

        self.usernameLabel = Label(self.loginForm, text="Username", font=("Arial bold", 13), bg=self.bgcolor, fg=self.fgcolor)
        self.usernameLabel.grid(row=1)

        self.usernameEntry = Entry(self.loginForm, font=("Calibri bold", 14), bg="#CDC2AE", fg="#293462")
        self.usernameEntry.grid(row=1, padx=10, pady=10, column=2)

        self.usernameLabel = Label(self.loginForm, text="Password", font=("Arial bold", 13), bg=self.bgcolor, fg=self.fgcolor)
        self.usernameLabel.grid(row=2)

        self.passwordEntry = Entry(self.loginForm, font=("Calibri bold", 14), bg="#CDC2AE", fg="#293462", show="*")
        self.passwordEntry.grid(row=2, padx=10, pady=10, column=2)

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
        
        self.NUMBER = IntVar()
        self.NAME = StringVar()
        self.GENDER = StringVar()
        self.COURSE = StringVar()
        self.SUBJECT = StringVar()
        self.PRILEM = IntVar()
        self.MIDTERM = IntVar()
        self.FINAL = IntVar()
        self.AVERAGE = IntVar()
        self.REMARK = StringVar()
        self.PE = IntVar()

        window = Toplevel()
        window.geometry("1600x1000")

        window.config(bg=self.bgcolor)


        self.guiFrame = Frame(window, bg=self.bgcolor)
        self.guiFrame.pack()

        self.universityLabel = Label(self.guiFrame, text="UNIVERSITY OF DRAGONS", font=("Calibri bold", 20), fg=self.fgcolor, bg=self.bgcolor)
        self.universityLabel.grid(padx=20, pady=20)

        self.listboxColumn = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')
        
        #self.style.configure("mystyle.Treeview", font=('Calibri bold', 11))
        
        self.listbox = Treeview(window, columns=self.listboxColumn, show='headings')
        

        self.listbox.heading('1', text="Student Number")
        self.listbox.heading('2', text="Name")
        self.listbox.heading('3', text="Gender")
        self.listbox.heading('4', text="Course")
        self.listbox.heading('5', text="Subject")
        self.listbox.heading('6', text="Prelim")
        self.listbox.heading('7', text="Midterm")
        self.listbox.heading('8', text="Final")
        self.listbox.heading('9', text="Average")
        self.listbox.heading('10', text="Remark")
        self.listbox.heading('11', text="PE")

        self.listbox.pack(padx=30, pady=30)

        self.listbox.bind('<Double-Button-1>', self.showValue)

        self.searchFrame = Frame(window, bg=self.bgcolor)
        self.searchFrame.pack()

        self.searchlbl = Label(self.searchFrame, text="Search Student:", bg=self.bgcolor,  font=('Calibri bold', 15), fg="#0AA1DD")
        self.searchlbl.grid(row=1, column=1, padx=10, pady=10)

        self.searchEntry = Entry(self.searchFrame, width=20, font=('Calibri bold', 15))
        self.searchEntry.grid(row=1, column=2, padx=10, pady=10)
        
        self.searchButton = Button(self.searchFrame, text="Search", bg="#14C38E", font=("Calibri bold", 15), command=self.searchStudent)
        self.searchButton.grid(row=1, column=3, padx=10, pady=10)



        parentFrame = Frame(window)
        parentFrame.pack()

        #Entry Frame for Student Information
        self.entryFrames = Frame(parentFrame, bg=self.bgcolor)
        self.entryFrames.grid(row=1, column=1)

        studentNolabel = Label(self.entryFrames, text="Student Number", font=('Calibri bold', 15), bg=self.bgcolor, fg="#3BACB6")
        studentNolabel.grid(row = 1)

        self.studentNoEntry = Entry(self.entryFrames, width=20, font=('Calibri bold', 13), textvariable=self.NUMBER)
        self.studentNoEntry.grid(row=2)

        studentNameLabel = Label(self.entryFrames, text="Student Name", font=('Calibri bold', 15), bg=self.bgcolor, fg="#3BACB6")
        studentNameLabel.grid(row = 3)

        self.studentnameEntry = Entry(self.entryFrames, width=20, font=('Calibri bold', 13), textvariable=self.NAME)
        self.studentnameEntry.grid(row=4)

        self.studentGenderLabel = Label(self.entryFrames, text="Student Gender", font=('Calibri bold', 15), bg=self.bgcolor, fg="#3BACB6")
        self.studentGenderLabel.grid(row = 5)

        self.studentGenderEntry = Combobox(self.entryFrames, width=20, font=('Calibri bold', 12), values=['Female', 'Male'], textvariable=self.GENDER)
        self.studentGenderEntry.grid(row=6)

        studentCourseLabel = Label(self.entryFrames, text="Student Course", font=('Calibri bold', 15), bg=self.bgcolor, fg="#3BACB6")
        studentCourseLabel.grid(row =7)

        self.studentCourseEntry = Combobox(self.entryFrames, width=20, font=('Calibri bold', 12), values=['BS Information Technology', 'Data Science', 'Computer Engineering', 'Civil Engineering'], textvariable=self.COURSE)
        self.studentCourseEntry.grid(row=8)

        studentSubjectLabel = Label(self.entryFrames, text="Student Subject", font=('Calibri bold', 15), bg=self.bgcolor, fg="#3BACB6")
        studentSubjectLabel.grid(row = 9)

        self.studentSubjectEntry = Entry(self.entryFrames, width=20, font=('Calibri bold', 13), textvariable=self.SUBJECT)
        self.studentSubjectEntry.grid(row=10)




        self.studentGrade = Frame(parentFrame, bg=self.bgcolor)
        self.studentGrade.grid(row=1, column=2)
        #colum 2

        studentPrelimLabel = Label(self.studentGrade, text="Student Prelim", font=('Calibri bold', 15), bg=self.bgcolor, fg="#3BACB6")
        studentPrelimLabel.grid(row = 1)

        self.studentPrelimEntry = Entry(self.studentGrade, width=20, font=('Calibri bold', 13), textvariable=self.PRILEM)
        self.studentPrelimEntry.grid(row=2)

        studentMidtermlabel = Label(self.studentGrade, text="Student MidTerm", font=('Calibri bold', 15), bg=self.bgcolor, fg="#3BACB6")
        studentMidtermlabel.grid(row = 3)

        self.studentMidtermEntry = Entry(self.studentGrade, width=20, font=('Calibri bold', 13), textvariable=self.MIDTERM)
        self.studentMidtermEntry.grid(row=4)

        studentFinallabel = Label(self.studentGrade, text="Student Final", font=('Calibri bold', 15), bg=self.bgcolor, fg="#3BACB6")
        studentFinallabel.grid(row = 5)

        self.studentFinalEntry = Entry(self.studentGrade, width=20, font=('Calibri bold', 13), textvariable=self.FINAL)
        self.studentFinalEntry.grid(row=6)

        studentAveragelabel = Label(self.studentGrade, text="Student Average",font=('Calibri bold', 15), bg=self.bgcolor, fg="#3BACB6")
        studentAveragelabel.grid(row = 7)

        self.studentAverageEntry = Entry(self.studentGrade, width=20, font=('Calibri bold', 13), textvariable=self.AVERAGE, state="disabled")
        self.studentAverageEntry.grid(row=8)

        studentRemarklabel = Label(self.studentGrade, text="Student Remark", font=('Calibri bold', 15), bg=self.bgcolor, fg="#3BACB6")
        studentRemarklabel.grid(row = 9)  

        self.studentRemarkEntry = Entry(self.studentGrade, width=20, font=('Calibri bold', 13), state="disabled",textvariable=self.REMARK)
        self.studentRemarkEntry.grid(row=10)

        studentpoinEquivalentLabel = Label(self.studentGrade, text="Student Point Equivalent", font=('Calibri bold', 15), bg=self.bgcolor, fg="#3BACB6")
        studentpoinEquivalentLabel.grid(row = 1, column=2)

        self.studentpoinEquivalentEntry = Entry(self.studentGrade, width=20, font=('Calibri bold', 13), state="disabled", textvariable=self.PE)
        self.studentpoinEquivalentEntry.grid(row=2, column=2)



        #create update delete frame
        crudButton = Frame(window, bg=self.bgcolor)
        crudButton.pack()

        saveButton = Button(crudButton, text="Save Student", command=self.createStudent, fg="#383838", bg="#00FFAB", font=('Calibri bold', 15))
        saveButton.grid(padx=10, pady=10, row=1,column=1)

        updateButton = Button(crudButton, text="Update Student", command=self.updateStudent, fg="#B4FF9F", bg="#242F9B", font=('Calibri bold', 15))
        updateButton.grid(padx=10, pady=10,row=1, column=2)

        deleteButton = Button(crudButton, text="Delete Student", command=self.deleteStudent, fg="#B4FF9F", bg="#FF5D5D", font=('Calibri bold', 15))
        deleteButton.grid(padx=10, pady=10, row=1, column=3)

        self.displayData()

        clearData = Button(window, text="Clear", command=self.clearData)
        clearData.pack()

    
    def displayData(self):
        display = self.student.displayData(listbox=self.listbox)

    def showValue(self, event):
        try:

            global tud_id
            f = self.listbox.focus()
            content = (self.listbox.item(f))
            selecteditem = content['values']
            self.stud_id = selecteditem[0]
            #print(self.stud_id)

            self.studentRemarkEntry.config(state="normal")
            self.studentpoinEquivalentEntry.config(state="normal")
            self.studentAverageEntry.config(state="normal")
            self.studentNoEntry.delete(0,'end')
            self.studentnameEntry.delete(0, 'end')
            self.studentGenderEntry.delete(0, 'end')
            self.studentCourseEntry.delete(0, 'end')
            self.studentSubjectEntry.delete(0, 'end')
            self.studentPrelimEntry.delete(0, 'end')
            self.studentMidtermEntry.delete(0, 'end')
            self.studentFinalEntry.delete(0, 'end')
            self.studentAverageEntry.delete(0, 'end')
            self.studentRemarkEntry.delete(0, 'end')
            self.studentpoinEquivalentEntry.delete(0, 'end')

            row_id = self.listbox.selection()[0]
            self.setlist = self.listbox.set(row_id)
            self.studentNoEntry.insert(0, self.setlist['1'])
            self.studentnameEntry.insert(0, self.setlist['2'])
            self.studentGenderEntry.insert(0, self.setlist['3'])
            self.studentCourseEntry.insert(0, self.setlist['4'])
            self.studentSubjectEntry.insert(0, self.setlist['5'])
            self.studentPrelimEntry.insert(0, self.setlist['6'])
            self.studentMidtermEntry.insert(0, self.setlist['7'])
            self.studentFinalEntry.insert(0, self.setlist['8'])
            self.studentAverageEntry.insert(0, self.setlist['9'])
            self.studentRemarkEntry.insert(0, self.setlist['10'])
            self.studentpoinEquivalentEntry.insert(0, self.setlist['11'])

            self.studentRemarkEntry.config(state="disabled")
            self.studentpoinEquivalentEntry.config(state="disabled")
            self.studentAverageEntry.config(state="disabled")
        except:
            messagebox.showerror(title="Select Data", message="Please select proper Data")
    
    def clearData(self):
        self.studentRemarkEntry.config(state="normal")
        self.studentpoinEquivalentEntry.config(state="normal")
        self.studentAverageEntry.config(state="normal")
        self.studentNoEntry.delete(0,'end')
        self.studentnameEntry.delete(0, 'end')
        self.studentGenderEntry.delete(0, 'end')
        self.studentCourseEntry.delete(0, 'end')
        self.studentSubjectEntry.delete(0, 'end')
        self.studentPrelimEntry.delete(0, 'end')
        self.studentMidtermEntry.delete(0, 'end')
        self.studentFinalEntry.delete(0, 'end')
        self.studentAverageEntry.delete(0, 'end')
        self.studentRemarkEntry.delete(0, 'end')
        self.studentpoinEquivalentEntry.delete(0, 'end')
        self.studentRemarkEntry.config(state="disabled")
        self.studentpoinEquivalentEntry.config(state="disabled")
        self.studentAverageEntry.config(state="disabled")

    def createStudent(self):
        if self.NAME.get() == "" or self.GENDER.get() == "" or self.COURSE.get() == "" or self.COURSE.get() == "" or self.SUBJECT.get() == "" or self.PRILEM.get() == "" or self.MIDTERM.get() == "" or self.FINAL.get() == "":
            messagebox.showerror(message="Please Fill the form", title="Please Try Again")
        else:
            f = self.listbox.focus()
            content = (self.listbox.item(f))
            selecteditem = content['values']
            self.stud_id = selecteditem[0]
            row_id = self.listbox.selection()[0]
            self.setlist = self.listbox.set(row_id)
            if self.studentNoEntry.get() == self.setlist['1']:
                messagebox.showerror(message="Student Already Exist", title="Student Existed, please change the Student Number")
            else:
                avg =(self.PRILEM.get() + self.MIDTERM.get() + self.FINAL.get()) / 3

                average = round(avg, 2)

                pe = self.pointeq(average=average)
                remarks = self.remarks(pe)
                #print(remarks)

                create = self.student.createStudent(self.NUMBER.get(), self.NAME.get(), self.GENDER.get(), self.COURSE.get(), self.SUBJECT.get(), self.PRILEM.get(), self.MIDTERM.get(), self.FINAL.get(), average, remarks, pe)

                if create:
                    messagebox.showinfo(message="Successfully Stored", title="Success")
                else:
                    messagebox.showerror(message="Please input correctly", title="Error")
            self.clearData()
            self.displayData()


    def pointeq(self, average):
        if average >= 96:
            return 1.00
        elif average >=95:
            return 1.25
        elif average >=93:
            return 1.50
        elif average >=91:
            return 1.75
        elif average >=88:
            return 2.00
        elif average >=86:
            return 2.25
        elif average >=83:
            return 2.75
        elif average >=78:
            return 2.75
        else:
            return 5.00

    def remarks(self, grade):
        match grade:
            case 1.00:
                return "Excellent"
            case 1.25:
                return "Very Good"
            case 1.50:
                return "Very Good"
            case 1.75:
                return "Good"
            case 2.00:
                return "Good"
            case 2.25:
                return "Good"
            case 2.50:
                return "Fair"
            case 2.75:
                return "Fair"
            case 3.00:
                return "Passed"
            case 5.00:
                return "Failed"
        
    def updateStudent(self):
        try:
            avg =(self.PRILEM.get() + self.MIDTERM.get() + self.FINAL.get()) / 3

            average = round(avg, 2)

            pe = self.pointeq(average=average)
            remarks = self.remarks(pe)
            update = self.student.updateStudent(self.NUMBER.get(), self.NAME.get(),self.GENDER.get(),self.COURSE.get(),self.SUBJECT.get(),self.PRILEM.get(),self.MIDTERM.get(),self.FINAL.get(), average,remarks,pe,self.stud_id)

            if update:
                messagebox.showinfo(message="Successfully Update", title="Successfully Update Student Information!")
            else:
                messagebox.showerror(message="Please Try Again", title="Please Try Again")
        except Exception as e:
            messagebox.showerror(message="Please try again. Double Check the data", title="Double Check the data")
        self.clearData()
        self.displayData()
    
    def deleteStudent(self):
        try:
            delete = self.student.deleteStudent(self.stud_id)
            if delete:
                messagebox.showinfo(message="Erased Data!",title="Successfully Erased")
        except Exception as e:
            messagebox.showerror(message="Please try again. Double Check the data", title="Double Check the data")
        self.clearData()
        self.displayData()
    
    def searchStudent(self):
        search = self.searchEntry.get()
        selections = []
        for child in self.listbox.get_children():
            if search in self.listbox.item(child)['values']:
                #print(self.listbox.item(child)['values'])
                selections.append(child)
        #print("search completed")
        self.listbox.selection_set(selections)

#a = Student(0)

#a.createStudent(0, 'Jaynel','BSIT', 'studentSubject', 90, 90,90,90,'Good',2.00)

    
if __name__ == "__main__":
    app = studenGUI()
    app.mainloop()