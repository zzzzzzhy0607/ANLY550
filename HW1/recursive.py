#### ANLY550 Homework1
#### Hongyang Zheng
import time


#### Question1 
#### Recursive
def recursive_Fnumber(n):
    
    if n==0:
        return(0)
    elif n==1:
        return(1)
    else:
        return(recursive_Fnumber(n-1)+recursive_Fnumber(n-2))

if __name__ == '__main__':

    #### Test the time for Fibonacci numbers 40
    start_time = time.time()
    f=recursive_Fnumber(40)%65536
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
        F.append(recursive_Fnumber(i)%65536)
        i=i+1
    print('The modulo of the largest Fibonacci number that can be computed by recursive method is: ')
    print(F[-1], 'with index', i-1)   

