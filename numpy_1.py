import numpy as np
#Create array from the list
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Array addition ", arr1+arr2)
#2D array
arr = np.array([[1, 2, 3, 8], [4, 5, 6, 7]])
print("Rows and columns", arr.shape)
print("Number of dimensions", arr.ndim)
print("Data type", arr.dtype)

print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.eye((4)))
print(np.full((3, 3), 5))
print("Creating sequnence number:", np.arange(1, 11, 2))
print("Printing diagnoal matrix:", np.diag([1, 2, 3]))
#Data type operations
#Specify dtype
arr = np.array([1, 2, 3], dtype=float)
print("Converting int to float ", arr)

#Convert dtype
# Specify dtype
arr = np.array([1, 2, 3], dtype=float)  # [1., 2., 3.]

# Convert dtype
arr = np.array([1.5, 2.7, 3.9])
print(arr.astype(int))  # [1 2 3]