from itertools import *
from random import *
matrix = [[randint(-100,100) for i in range(3)] for f in range(3)]
a = [i for i in permutations("012",3)]
def Print(matrix):
    for i in range(3):
        for j in range(3):
            print(matrix[i][j],end = (5-len(str(matrix[i][j])))*" ")
        print()
def E(k):
    c =0
    for i in range(3):
       for j in range(i+1,3):
          if k[i]>k[j]:
              c+=1
    return 1 if c%2==0 else -1
def Det(matrix):
    det = 0
    for i in range(6):
        mt = 1
        for j in range(3):
            mt*=matrix[j][int(a[i][j])]
        det+=E(a[i])*mt
    return det
Print(matrix)
if Det(matrix)==0:

    print("строки матрицы","линейно-зависимы")
else:
    print("строки матрицы", "линейно-независимы")
