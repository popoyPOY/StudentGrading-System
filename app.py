from tkinter import messagebox
import sqlite3

DATABASE = "Database.db" #student Table

database = sqlite3.connect(DATABASE)

cursor = database.cursor()

class Student:
    def __init__(self, stud_id):
        self.stud_id = stud_id
        #self.studentName = studentName

    def createStudent(self, studentNo, StudentName, studentCourse, 
                    studentSubject, studentPrilem, studentMidterm,
                    studentFinal, studentAverage, studentRemark, 
                    studentpointEquivalent):
                    sql = '''INSERT INTO student (studno, studname, course, subject, prelim_grade, 
                                        midterm_grade, final_grade, average_grade, remark, point_equivalent)
                                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                    value = (studentNo, StudentName, studentCourse,
                            studentSubject, studentPrilem, studentMidterm,
                            studentFinal, studentAverage, studentRemark,
                            studentpointEquivalent)
                    try:
                        database.execute(sql, value)
                        database.commit()
                        database.close()
                        return True
                    except Exception as e:
                        print(e)
                        database.close()


    def updateStudent(self, studentNo, StudentName, studentCourse, 
                    studentSubject, studentPrilem, studentMidterm,
                    studentFinal, studentAverage, studentRemark, 
                    studentpointEquivalent):
                    sql = """UPDATE student SET studno = ?, studname = ?, course = ?, 
                                    subject = ?, prelim_grade = ?, midterm_grade = ?,
                                    final_grade = ?, average_grade = ?, remark = ?,
                                    point_equivalent = ? where stud_id = ?"""
                    value = (studentNo, StudentName, studentCourse,
                            studentSubject, studentPrilem, studentMidterm,
                            studentFinal, studentAverage, studentRemark,
                            studentpointEquivalent, self.stud_id)
                    try:
                        database.execute(sql, value)
                        database.commit()
                        database.close()
                        return True
                    except Exception as e:
                        messagebox.showerror(title="Error", message="Please Review Your Input")
                        print(e)
                        database.close()
    
    def deleteStudent(self):
        try:
            sql = "DELETE from student where stud_id = ?"
            value = (int(self.stud_id),)
            database.execute(sql, value)
            database.commit()
            database.close()
            return True
        except Exception as e:
            database.close()
            print(e)

    def searchStudent(self, studentNumber):
        try:
            sql = "SELECT * from student where studno = ?"
            value = (int(studentNumber),)
            cursor.execute(sql, value)
            
            #return a list
            return cursor.fetchall()
        except Exception as e:
            database.close()
            print(e)

    @staticmethod
    def createAccount(username, password):
        try:
            sql = "INSERT INTO users (username, password) VALUES (?, ?)"
            value = (username, password,)

            database.execute(sql, value)
            database.commit()
            database.close()
        
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
                    

