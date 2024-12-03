import numpy as np

# arr = np.arange(0,11)
#
# print(arr)
#
# sliced_array = arr[0:5]
#
# print('sliced array:', sliced_array)
#
# copied_array = arr.copy()
#
# copied_array[:] = 7 # cambiar todos los valores de un array
#
# print('copied array:', copied_array)
#
# matriz = np.array([[5,10,15], [20,25,30], [35,40,45]], dtype=int)
#
# print(matriz)
#
# print(matriz[0,1]) # otra manera de acceder a los valores de una matriz
#
# sliced_matriz = matriz[1:,:2] # obtener una sección de la matriz
#
# print(sliced_matriz)

matriz = np.arange(50).reshape(5,10)

print(matriz)

new_matriz = matriz[2:,5:
             ]
# print(new_matriz)

new_matriz2 = matriz[0:,5:]

print(new_matriz2)