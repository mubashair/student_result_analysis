import numpy as np
#-----------------------------------
# Student Information
#-----------------------------------

students = np.array([
     "Ali",
    "Ahmed",
    "Sara",
    "Fatima",
    "Usman",
    "Ayesha",
    "Bilal",
    "Zain"
])
subjects = np.array([
    "English",
    "Math",
    "Physics",
    "Chemistry",
    "Computer"
])
#This is 2D array each row represent one student
# and each column respresent one subject
# rows = students
# columns = subjects
marks = np.array([
    [78, 88, 80, 76, 90],
    [45, 55, 40, 60, 50],
    [90, 86, 91, 84, 88],
    [95, 98, 96, 97, 99],
    [65, 72, 68, 60, 70],
    [81, 79, 85, 83, 80],
    [35, 42, 30, 38, 40],
    [88, 84, 90, 86, 89]
])
print(marks.shape)
print("=" * 80)
print("             STUDENT RESULT MANAGEMENT SYSTEM")
print("=" * 80)
#Create the table header
header = f"{'Name':12}"
#add each subject name to the header
for sub in subjects:
    header = header + f"{sub:12}"
print(header)
print("-"*80)
#Loop through every student
for i in range(len(students)):
    #start the row with the student's name
    row = f"{students[i]:12}"
    #add each subject mark to the row
    for mark in marks[i]:
        row = row + f"{mark:12}"
    print(row)
    
