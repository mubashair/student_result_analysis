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
    Average       :{average[i]:.2f}
    Percentage    :{percentage[i]:.2f}%
    Grade         :{grade(average[i])}
    """)

print("CLASS STATISTICS")
print("=" * 40)
print(f"Total Students: {marks.shape[0]}")
print(f"Total Subjects: {marks.shape[1]}")
print(f"Total marks: {np.sum(marks)}")
print(f"Highest Marks: {np.max(marks)}")
print(f"Lowest Marks: {np.min(marks)}")
print(f"Class Average: {np.mean(marks):.2f}")
print(f"Median Marks: {np.median(marks):.2f}")
print(f"Standard Deviation: {np.std(marks):.2f}")

# ------------------------------------
# Subject Average
# ------------------------------------

print("\nSubject Average")

subject_average = np.mean(marks, axis=0)

for sub, avg in zip(subjects, subject_average):
    print(f"{sub:12} {avg:.2f}")

#---------------------------------
#Method 2 using pandas library
#---------------------------------
data_frame = pd.DataFrame(marks, columns=subjects)
print("\n Subject Average using pandas")
print(data_frame.mean())

# --- Method 2: Manual Calculation (to show the steps) ---
print("\n" + "=" * 50)
print("Manual Calculation (for understanding)")
print("=" * 50)
# 1. Sum per subject
subject_sum = np.sum(marks, axis=0)
# 2. Number of students
num_students = marks.shape[0]  # 8
# 3. Average
manual_avg = subject_sum / num_students

print("\nManual Subject Averages:")
for sub, avg in zip(subjects, manual_avg):
    print(f"{sub:12} {avg:.2f}")
#Subject Topper
print("\nSubject Topper")

for i in range(len(subjects)):
    topper = np.argmax(marks[:, i])
    print(subjects[i],
          "->",
          students[topper],
          "(",
          marks[topper, i], 
          ")"
         )
print("\n Class Topper")
topper = np.argmax(total)
print("Student:", students[topper])
print("Marks:  ", total[topper])

# ------------------------------------
# Pass / Fail with Marks
# ------------------------------------

print("\n" + "=" * 50)
print("PASSED STUDENTS")
print("=" * 50)
# 1. Create a boolean mask for passed students (average >= 50)
passed = average >= 50

# Filter arrays using the boolean mask
passed_names = students[passed] #only names of passed students
passed_totals = total[passed] #only total of passed students
passed_avgs = average[passed] #only average of passed students
#Print the formatted table header
print(f"{'Name':10} {'Total':>6} {'Average':>8} {'Grade'}")
print("-" * 35)

for name, tot, avg in zip(passed_names, passed_totals, passed_avgs):
    print(f"{name:10} {tot:6d} {avg:8.2f} {grade(avg):>6}")

print("\n" + "=" * 50)
print("FAILED STUDENTS")
print("=" * 50)

failed = average < 50

failed_names = students[failed]
failed_totals = total[failed]
failed_avgs = average[failed]

print(f"{'Name':10} {'Total':>6} {'Average':>8} {'Grade'}")
print("-" * 35)

for name, tot, avg in zip(failed_names, failed_totals, failed_avgs):
    print(f"{name:10} {tot:>6d} {avg:8.2f} {grade(avg):>6}")

# ------------------------------------
# Ranking
# ------------------------------------

print("\n")
print("=" * 80)
print("CLASS RANKING")
print("=" * 80)

rank = np.argsort(total)[::-1]

for i in range(len(rank)):
    index = rank[i]

    print(
        f"{i+1}. "
        f"{students[index]:10}"
        f" Total={total[index]}"
        f" Average={average[index]:.2f}"
    )
# ------------------------------------
# Search Student
# ------------------------------------

name = input("\nEnter Student Name : ")

index = np.where(students == name)

if len(index[0]) > 0:

    i = index[0][0]

    print("\nStudent Found")

    print("---------------------")

    print("Name :", students[i])

    for sub, mark in zip(subjects, marks[i]):
        print(sub, ":", mark)

    print("Total :", total[i])

    print("Average :", average[i])

    print("Grade :", grade(average[i]))

else:
    print("Student Not Found")