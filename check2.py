#Check If Questions Are Inserted
import sqlite3

conn = sqlite3.connect(r"C:\My_coding_journey\Final_Projects\GO_Tutorial\go_beginner_project_techwithtim\test.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM questions LIMIT 5;")
rows = cursor.fetchall()

if rows:
    for row in rows:
        print(row)
else:
    print("Error: No questions found in the database.")

conn.close()

