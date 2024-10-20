'''
Mark Ma
Ghidorah - Mark, Danny, Marco
SoftDev
K19 - sqlite3 and DictReader
2024-10-08
time spent: 1
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="discobandit.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

courses_info = csv.DictReader(open("courses.csv"))
students_info = csv.DictReader(open("students.csv"))

c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);")
for x in students_info:
    print(x)
    c.execute(f'INSERT INTO students  VALUES (\'{x["name"]}\', {int(x["age"])}, {int(x["id"])});') #Put quotes around string variable so db recognizes it as a data value rather than a column name
c.execute("CREATE TABLE courses (name TEXT, mark INTEGER, id INTEGER);")
for y in courses_info:
    print(y)
    c.execute(f'INSERT INTO courses VALUES (\'{y["code"]}\', {int(y["mark"])}, {int(y["id"])});')



#==========================================================

db.commit() #save changes
db.close()  #close database
