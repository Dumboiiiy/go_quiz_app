# Check If the Table Exists
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect(r"C:\My_coding_journey\Final_Projects\GO_Tutorial\go_beginner_project_techwithtim\test.db")
cursor = conn.cursor()

# Check if the 'questions' table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='questions';")
table_exists = cursor.fetchone()

if table_exists:
    print("Table 'questions' exists.")
else:
    print("Error: Table 'questions' does not exist!")

conn.close()
