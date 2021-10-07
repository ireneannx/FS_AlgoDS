import numpy as np

# Write a Python program to create a null vector of size 10 but the fifth value which is 1.
x = np.zeros(10)
x[4] = 1
# print(x)

#  Write a Python program to generate six random integers between 10 and 30.
y = np.random.randint(10, 31, 6)
# print(y)

# Write a Python program to create a 3x3x3 array with random values.
z = np.random.random((3, 3, 3))

# Write a Python program to create a 3x3 matrix with values ranging from 0 to 8.
a = np.random.randint(0, 9, (3, 3))
# print(a)

# Write a Python program to create a random 10x4 array and extract the first five rows of the array and store
# them into a variable
b = np.floor(10 * np.random.random((10, 4)))
c = b[:5]
# print(c)

#  Write a Python program to create a 2-dimensional array with 1 on the border and 0 inside.
d = np.zeros((3, 4))

for row_index in range(np.shape(d)[0]):  # rows
    for col_index in range(np.shape(d)[1]):  # cols
        if row_index == 0 or row_index == np.shape(d)[0] - 1 or col_index == 0 or col_index == np.shape(d)[1] - 1:
            d[row_index][col_index] = 1

print(d)


