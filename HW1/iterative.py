#### ANLY550 Homework1
#### Hongyang Zheng
import time


#### Question1 
#### Iterative 
def iterative_Fnumber(n):
     
    # List to store Fibonacci number
    F=[]
    # Store F(0)
    F.append(0)
    # Store F(1)
    F.append(1)
    
    if n==0:
        return(F[n])
    elif n==1:
        return(F[n])
    else:
        # Calculate Fibonacci number when n>=2
        for i in range(2,n+1):
            F.append(F[i-1]+F[i-2])   
        f=F[n]%65536
        return(f)

if __name__ == '__main__':

    #### Test the time for Fibonacci numbers 40
    start_time = time.time()
    f=iterative_Fnumber(40)
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
        F.append(iterative_Fnumber(i))
        i=i+1
    print('The modulo of the largest Fibonacci number that can be computed by iterative method is: ')
    print(F[-1], 'with index', i-1)   