#Ensure test.db is the Correct Database
import os
db_path = r"C:\My_coding_journey\Final_Projects\GO_Tutorial\go_beginner_project_techwithtim\test.db"

if os.path.exists(db_path):
    print(f"Database found at: {db_path}")
else:
    print("Error: Database file not found!")
