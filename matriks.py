import numpy
import sys
import numpy as np


#Matrix in Python using list
matriks = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
            
print(matriks)

    
print("======================")
#Matrix in Python using Array from Numpy library

matriks2 = numpy.array([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]])
            
print(matriks2)


print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(matriks)*len(matriks))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", matriks2.size*matriks2.itemsize)


print("======================")
#Akses matrix

var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
           
print(var_mat[2][1])

print("======================")
#Multiple calculation in Matrix

#generic method, without library
var_mat = [[5, 0],
          [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
  for j in range(len(var_mat[0])):
    def_mat[i][j] = var_mat[i][j]*2

print(def_mat)


#With numpy library

var_mat2 = np.array([[5, 0],[1, -2]])

result = var_mat2*2

print (result)