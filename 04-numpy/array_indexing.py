import numpy as np

arr = np.arange(0,11)

print(arr)

sliced_array = arr[0:5]

print('sliced array:', sliced_array)

copied_array = arr.copy()

copied_array[:] = 7 # cambiar todos los valores de un array

print('copied array:', copied_array)

matriz = np.array([[5,10,15], [20,25,30], [35,40,45]], dtype=int)

print(matriz)