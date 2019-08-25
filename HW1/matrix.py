#### ANLY550 Homework1
#### Hongyang Zheng
import time

#### Question1 
#### Matrix
#### Function to multiply matrix
def Matrix_Multiply(A,F):
    
    a11 = A[0][0] * F[0][0] + A[0][1] * F[1][0]
    a12 = A[0][0] * F[0][1] + A[0][1] * F[1][1]
    a21 = A[1][0] * F[0][0] + A[1][1] * F[1][0]
    a22 = A[1][0] * F[0][1] + A[1][1] * F[1][1]
    
    A[0][0] = a11 
    A[0][1] = a12
    A[1][0] = a21
    A[1][1] = a22
    
    return(A) 

#### Function to calculate Fibonacci numbers    
def Matrix_Fnumber(n):
    
    # Create default matrix
    A=[[0,1],
       [1,1]]
    
    F=[[0,1],
       [1,1]]
    
    # Base case
    if n==0:
        return(0)
        
    # Base case    
    elif n==1:
        return(1)
        
    # If n is even number
    elif n%2==0:
        mid=int(n/2)
        # Calculate A^(n/2) first
        for i in range(1,mid):
            A=Matrix_Multiply(A,F)
        # Square A^(n/2) to get A^n
        A=Matrix_Multiply(A,A) 
        
        # Find modulo
        f=A[0][1]%65536
        return(f)
        
    # If n is odd number
    elif n%2!=0:
        mid=int((n-1)/2)
        # Calculate A^((n-1)/2)
        for i in range(1,mid):
            A=Matrix_Multiply(A,F)
        # Square A^((n-1)/2) to get A^(n-1)
        A=Matrix_Multiply(A,A)
        # Multiple A one more time to get A^n
        A=Matrix_Multiply(A,F)
        
        # Find modulo
        f=A[0][1]%65536
        return(f)

if __name__ == '__main__':

    #### Test the time for Fibonacci numbers 40
    start_time = time.time()
    f=Matrix_Fnumber(40)
    print("--- %s seconds ---" % (time.time() - start_time))

    #### Test the largest number this method can compute in one minute of machine time
    # One minute machine time
    time_end = time.time() + 60 
    # Starting from F0
    i=0
    # Store Fibonacci series
    F=[]
    # While loop to calculate Fibonacci numbers
    while time.time() < time_end:   
        F.append(Matrix_Fnumber(i))
        i=i+1
    print('The modulo of the largest Fibonacci number that can be computed by matrix method is: ')
    print(F[-1], 'with index', i-1)   