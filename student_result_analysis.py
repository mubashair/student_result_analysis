import numpy as np
#Numpy is used numerical calculations and array operations
#Creating numpy array containing students name
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
# ======================================================
# Student Marks
# ======================================================
# Create another NumPy array containing marks.
# Each mark corresponds to the student at the same index.
marks = np.array([85, 42, 67, 91, 55, 73, 38, 80])
print("=" * 40)
print("STUDENT RESULT SYSTEM")
print("=" * 40)

# Loop through every student using its index.
for i in range(len(students)):
    #Display student name and marks
    #:10 reserve 10 spaces for name
    print(f"{students[i]:10}:{marks[i]}")


# ======================================================
# Statistics
# ======================================================

print("\n------ Statistics ------")

# Total number of students
print("Total Students :", len(students))
#Highest marks in the array
print("Highest marks:", np.max(marks))
#Lowest marks in the array
print("Highest marks:", np.min(marks))

# Average marks
print("Average Marks  :", np.mean(marks))

# Sum of all marks
print("Total Marks    :", np.sum(marks))

# Middle value after sorting
print("Median         :", np.median(marks))

# Standard deviation tells how spread out the marks are.
# round(...,2) displays only 2 decimal places.
print("Standard Dev   :", round(np.std(marks), 2))

#Creat a Boolean array 
#True means marks are greater than or equal to 50
passed = marks >= 50
#use boolean indexing to display only passed students
for name, mark in zip(students(passed), marks(passed)):
    print(name, "-", mark)