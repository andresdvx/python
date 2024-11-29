import numpy as np

# mylist = [1,2,3]
#
# print(mylist)
#
# array = np.array(mylist) # crear un array
#
# print(array)
#
# mymatrix = [ [1,2,3], [4,5,6],[7,8,9] ] # crear una matriz
#
# print(mymatrix)
#
# matrix = np.array(mymatrix)
#
# print(matrix)
#
# print(matrix[2][1])
#
# arange = np.arange(0, 11, 2) # crear un array con rangos definidos
#
# print(arange)
#
# zero_martix = np.zeros((3,3)) # crear una matriz de 0 pasandole una tupla con las dimensiones
#
# print(zero_martix)
#
# ones_martrix = np.ones((2,2))  # crear una matriz de 1 pasandole una tupla con las dimensiones
#
# print(ones_martrix)
#
# straing_array = np.array(["andres","pacheco", "cuadro"])
#
# print(straing_array.dtype)
# --------------------------------------------------
#
# arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
#
# copy_arr = arr.copy() # copiar un array
#
# view_array = arr.view() # crear una vista de un array
#
# print('original array:', arr)
# print('copy array:', copy_arr)
# print('view array:', view_array)
#
#
# print('matrix row, colums',arr.shape) # obtener el número de filas y columnas de la matriz

array_to_reshape = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(array_to_reshape)

reshaped_array = array_to_reshape.reshape(4,3)

print(reshaped_array)