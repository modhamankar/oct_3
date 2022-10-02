import numpy as nps
# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [745, 8, 9]]
 
# take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 134]]
 
# result will be 3x4
 
result= [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
 
result = nps.dot(A,B)
 
for r in result:
    print(r)
