from tkinter import messagebox
import sqlite3


DATABASE = "Database.db" #student Table

database = sqlite3.connect(DATABASE)

class Student:
    def __init__(self):
        self.stud_id = None
    

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
                        messagebox.showinfo(title="Sucess", message="Done!")
                        database.close()
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
                                    point_equivalent = ?"""
                    value = (studentNo, StudentName, studentCourse,
                            studentSubject, studentPrilem, studentMidterm,
                            studentFinal, studentAverage, studentRemark,
                            studentpointEquivalent)
                    try:
                        database.execute(sql, value)
                        database.commit()
                        messagebox.showinfo(title="Sucess", message="Done!")
                        database.close()
                    except Exception as e:
                        print(e)
                        database.close()




                    

