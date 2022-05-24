import sqlite3



def Database():
    global conn, cursor 
    
    conn = sqlite3.connect('Database.db')
    
    conn.execute('''
        CREATE TABLE student (stud_id INT PRIMARY KEY AUTOINCREMENT NOT NULL,
                              studno INT,
                              studname TEXT,
                              course TEXT,
                              subject TEXT,
                              prelim_grade INT,
                              midterm_grade INT,
                              final_grade INT,
                              average_grade INT,
                              remark TEXT,
                              point_equivalent TEXT)
                              
                ''')
    conn.commit()
    conn.close()

Database()
