import numpy
import sys


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