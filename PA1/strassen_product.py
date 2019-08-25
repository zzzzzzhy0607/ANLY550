#!/usr/bin/python3
# -*- coding: utf-8 -*-

### ANLY550 - PS3: Programming Assignment
### Heng Zhou, Hongyang Zheng


# Import necessary libraries
import sys


# Funtion to determine whether the matrix is odd or even
def strassen_even(A, B):
    n = len(A)
    
    # Conventional matrix multiplicaton
    if n <= CrossOverPoint:
        return conventional_product(A, B)
    
    # If dimension is even, perform strassen directly
    if n % 2 == 0:
      
        # Calculate the sub-matrix size
        sub_size = int(n/2)
        
        # Dividing matrix A into 4 sub-matrices
        a11 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
        a12 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
        a21 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
        a22 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
        
        # Dividing matrix B into 4 sub-matrices
        b11 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
        b12 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
        b21 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]
        b22 = [[0 for j in range(0, sub_size)] for i in range(0, sub_size)]

        # Put values into the sub-matrices
        for i in range(0, sub_size):
            for j in range(0, sub_size):
                # Top left
                a11[i][j] = A[i][j]  
                # Top right      
                a12[i][j] = A[i][j + sub_size]     
                # Bottom left
                a21[i][j] = A[i + sub_size][j]  
                # Bottom right
                a22[i][j] = A[i + sub_size][j + sub_size]  
                
                # Top left
                b11[i][j] = B[i][j]    
                # Top right    
                b12[i][j] = B[i][j + sub_size]      
                # Bottom left
                b21[i][j] = B[i + sub_size][j]      
                # Bottom right
                b22[i][j] = B[i + sub_size][j + sub_size]  

        # Calculating p1 to p7
        p1 = strassen_even(add(a11, a22), add(b11, b22))          # p1 = (a11+a22) * (b11+b22)
        p2 = strassen_even(add(a21, a22), b11)                    # p2 = (a21+a22) * (b11)
        p3 = strassen_even(a11, subtract(b12, b22))               # p3 = (a11) * (b12 - b22)
        p4 = strassen_even(a22, subtract(b21, b11))               # p4 = (a22) * (b21 - b11)
        p5 = strassen_even(add(a11, a12), b22)                    # p5 = (a11+a12) * (b22)
        p6 = strassen_even(subtract(a21, a11), add(b11, b12))     # p6 = (a21-a11) * (b11+b12)
        p7 = strassen_even(subtract(a12, a22), add(b21, b22))     # p7 = (a12-a22) * (b21+b22)

        # Calculating c11, c12, c21, c22
        c11 = subtract(add(add(p1, p4), p7), p5)                # c11 = p1 + p4 - p5 + p7
        c12 = add(p3, p5)                                       # c12 = p3 + p5
        c21 = add(p2, p4)                                       # c21 = p2 + p4
        c22 = subtract(add(add(p1, p3), p6), p2)                # c22 = p1 + p3 - p2 + p6

        # Combine the results to a single matrix
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, sub_size):
            for j in range(0, sub_size):
                # Top left
                C[i][j] = c11[i][j]         
                # Top right
                C[i][j + sub_size] = c12[i][j]      
                # Bottom left
                C[i + sub_size][j] = c21[i][j]     
                # Bottom right
                C[i + sub_size][j + sub_size] = c22[i][j]  
        return C
      
    # If n is odd
    elif n % 2 != 0:
        C = strassen_odd(A, B)   
        return C

   
def strassen_odd(A, B):
    assert type(A) == list and type(B) == list
    assert len(A) == len(A[0]) == len(B) == len(B[0])

    # Pad one row and one column with 0s   
    n = len(A)
    m = n + 1
    A1 = [[0 for i in range(m)] for j in range(m)]
    B1 = [[0 for i in range(m)] for j in range(m)]
    for i in range(n):
        for j in range(n):
            A1[i][j] = A[i][j]
            B1[i][j] = B[i][j]
    C1 = strassen_even(A1, B1)
    
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = C1[i][j]
    return C


# Compute the product of matrix by traditional method, assuming squared matrices
def conventional_product(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Helper to perform the addition of matrix
def add(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C


# Helper to perform the subtraction of matrix
def subtract(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C


if __name__ == "__main__":
    # Take the arguments 
    if sys.argv[1] != "0" or len(sys.argv) != 4:
        print("Input 'python your_python_file.py 0 dimension inputfile'!")
    else:
        dimension = sys.argv[2]
        filename = sys.argv[3]
    
    # Create two lists to store the elements in each matrix
    listA = []
    listB = []
    with open(filename, 'r') as f:
        for line in f:
            if len(listA) < int(dimension)**2:
                listA.append(int(line))
            else:
                listB.append(int(line))
                
    # Convert listA and listB to matrix A and matrix B
    A = [[0 for j in range(int(dimension))] for i in range(int(dimension))]
    B = [[0 for j in range(int(dimension))] for i in range(int(dimension))]
    for i in range(int(dimension)):
        for j in range(int(dimension)):
            A[i][j] = listA[i*int(dimension)+j]
            B[i][j] = listB[i*int(dimension)+j]
    
    # Set Cross point, for example 32
    CrossOverPoint = 32
    C = strassen_even(A, B)
    for i in range(int(dimension)):
            print(C[i][i])