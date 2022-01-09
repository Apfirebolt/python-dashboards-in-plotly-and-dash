import numpy as np

my_list = [0,1,2,3,4]

arr = np.array(my_list)

# Converts a normal list into numpy array
print(arr)

# Create an numpy array in a given range
a = np.arange(0,10)
print(a)

# Ranged numpy array with step
a= np.arange(0,10,2)
print(a)

# Create array of 0s and 1s

# a = np.zeros((5, 2))
# print(a)

# a = np.ones((2,4))
# print(a)

# Random numbers with numpy
a = np.random.randint(0,10)
print(a)

# Create 2d matrix of random ints
a = np.random.randint(0,10,(3,3))
print(a)

# 1D array of random numbers
a = np.random.randint(0, 20, (7))
print(a)

# Max, Min and Mean of an array/list in numpy
print(a.max(), a.min(), a.mean())

# Min and Max locations
print(a.argmax(), a.argmin())

# Generate an array of 25 elements and convert into 10*10 matrix through reshape
mat = np.random.randint(0, 20, (25)).reshape(5, 5)
row = 2
col = 1

print(mat)

# Selecting an individual number:
print(mat[row,col])

# Select an entire column (all row entries of this column "col")
print(mat[:,col])

# Select an entire column (all row entries of this column "col")
print(mat[row,:])