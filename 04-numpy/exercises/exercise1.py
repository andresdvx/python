import numpy as np

# create an array of 10 zeros

# zero_array = np.zeros(10) #create an array of 10 zeros
#
# print(zero_array)
#
# ones_array = np.ones(10) #create an array of 10 ones
#
# print(ones_array)
#
# fives_array = np.ones(10) * 5 #create an array of 10 fives
#
# print(fives_array)
#
# integers_array = np.arange(10, 51, 1) #create an array of integers from 10 to 50
#
# print(integers_array)
#
# integers_array2 = np.arange(10, 51, 2) #create an array of all even integer from 10 to 50
#
# print(integers_array2)
#
# martrix = np.arange(9, dtype=int).reshape((3, 3)) #create an 3x3 matrix values ranging 0 to 8
#
# print(martrix)

identity_matrix = np.eye(3) #create an 3x3 identity matrix

print(identity_matrix)

random_number = np.random.rand(1) #create a random number

print(random_number)

randomValues_array = np.random.randn(25) #generate an array of 25 random numbers

print(randomValues_array)

mat = np.arange(1, 101).reshape((10,10)) / 100

print(mat)

linspace = np.linspace(0.01,1, 100).reshape(10, 10)

print(linspace)