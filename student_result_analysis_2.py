import numpy as np
import pandas as pd
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
    
######### Best Formating ########
# Create DataFrame with students as a column from the start
print("-"*80)
print("Table formating with padas library")
data_frame = pd.DataFrame(marks, index=students, columns=subjects)
data_frame.insert(0, 'Student Name', students)#inset name as first column
print(data_frame.to_string(index=False))

#Calculate the total marks for every student
#axis=1 means perform the calculation across each row
total = np.sum(marks, axis=1)
#Calculate the average marks for every student
average = np.mean(marks, axis=1)
#Calculate the percentage
percentage = total/(len(subjects)*100) *100

# Display results with formatting
print("="*70)
print("Student Performance Analysis")
print("="*70)
print(f"{'Student':<12} {'Total':<12} {'Average':<12} {'percentage'}")
#Display each student's result
for i in range(len(students)):
    print(f"{students[i]:<12} {total[i]:<12} {average[i]:<12.2f} {percentage[i]:5.2f}%")

#Grade function
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg > 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

#Student Report 
print("\n")
print("=" * 70)
print("STUDENT REPORT")
print("=" * 70)

for i in range(len(students)):
    print(f"""
    Student:{i+1}     :{students[i]}
    Total         :{total[i]}
    Average       :{average[i]}
    Percentage    :{percentage[i]:.2f}
    Grade         :{grade(average[i])}
    """)