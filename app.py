from tkinter import messagebox
import sqlite3

from sqlalchemy import values

DATABASE = "Database.db" #student Table

database = sqlite3.connect(DATABASE)

cursor = database.cursor()


class Student:
    def __init__(self, stud_id):
        self.stud_id = stud_id
        #self.studentName = studentName

    def createStudent(self, studentNo, StudentName, studentGender, studentCourse, 
                    studentSubject, studentPrilem, studentMidterm,
                    studentFinal, studentAverage, studentRemark, 
                    studentpointEquivalent):
                    sql = '''INSERT INTO student (studno, studname, studentgen, course, subject, prelim_grade, 
                                        midterm_grade, final_grade, average_grade, remark, point_equivalent)
                                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                    value = (studentNo, StudentName, studentGender, studentCourse,
                            studentSubject, studentPrilem, studentMidterm,
                            studentFinal, studentAverage, studentRemark,
                            studentpointEquivalent)
                    try:
                        database.execute(sql, value)
                        database.commit()
                        #database.close()
                        return True
                    except Exception as e:
                        raise e
                        #database.close()


    def updateStudent(self, studentNo, StudentName, studentGender, studentCourse, 
                    studentSubject, studentPrilem, studentMidterm,
                    studentFinal, studentAverage, studentRemark, 
                    studentpointEquivalent, stud_id):
                    sql = """UPDATE student SET studno = ?, studname = ?,studentgen = ?, course = ?, 
                                    subject = ?, prelim_grade = ?, midterm_grade = ?,
                                    final_grade = ?, average_grade = ?, remark = ?,
                                    point_equivalent = ? where studno = ?"""
                    value = (studentNo, StudentName, studentGender, studentCourse,
                            studentSubject, studentPrilem, studentMidterm,
                            studentFinal, studentAverage, studentRemark,
                            studentpointEquivalent, stud_id)
                    try:
                        database.execute(sql, value)
                        database.commit()
                        #database.close()
                        return True
                    except Exception as e:
                        messagebox.showerror(title="Error", message="Please Review Your Input")
                        print(e)
                        database.close()
    
    def deleteStudent(self, stud_id):
        try:
            sql = "DELETE from student where studno = ?"
            value = (int(stud_id),)
            database.execute(sql, value)
            database.commit()
            #database.close()
            return True
        except Exception as e:
            #database.close()
            print(e)

    def searchStudent(self, studentNumber):
        try:
            sql = "SELECT * from student where studno = ?"
            value = (int(studentNumber),)
            cursor.execute(sql, value)
            
            #return a list
            return cursor.fetchall()
        except Exception as e:
            #database.close()
            print(e)

    def displayData(self, listbox):
        listbox.delete(*listbox.get_children())
        cursor.execute("SELECT * from `student` ORDER BY `studno` ASC")
        #database.commit()
        fetchdata = cursor.fetchall()

        for data in fetchdata:
            listbox.insert('', 'end', values=(data[1], data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10], data[11]))
        
            #print(data)
        #database.close()

    @staticmethod
    def createAccount(username, password):
        try:
            sql = "INSERT INTO users (username, password) VALUES (?, ?)"
            value = (username, password,)

            database.execute(sql, value)
            database.commit()
            #database.close()
        
        except Exception as e:
            print(e)
    
    @staticmethod
    def loginAccount(username, password):
        if username == '' and password == '':
            messagebox.showerror(title="Please Try Againa", message="Please fill the Form")
        else:
            conn = database.execute("SELECT * from users WHERE username = ? AND password = ?", (username, password,))
            if conn.fetchone():
                return True
            else:
                messagebox.showerror(title="Invalid Login", message="Invalid username or password")



#student = Student(0)
#student.createAccount("admin", "admin")
#student.createStudent(1,'Jaynel', 'Male', 'BSIT', 'Prog2', 90,90,90, 90, 'Good', 2.00)
                    

