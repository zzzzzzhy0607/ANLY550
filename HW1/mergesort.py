#### ANLY550 Homework1
#### Hongyang Zheng
import sys

#### Question7
#### Merge Sort
#### Assume the size of A is a power of two     
def MergeSort(A):
    
    if len(A)>1:
        # Get the middle index of the array 
        mid_n = int(len(A)/2)
        # Separate the array into two subarrays
        B=A[:mid_n]
        C=A[mid_n:]
        # Recursively using MergeSort for the two subarrays
        MergeSort(B)
        MergeSort(C)

        # Merge Process
        i=0
        j=0
        k=0        
        n1=len(B)
        n2=len(C)
        
        # Merge 
        while i < n1 and j < n2:
            if B[i]<C[j]:
                    A[k]=B[i]           
                    i=i+1
            else:
                    A[k]=C[j]
                    j=j+1
            k=k+1
        
        # If there is any left numbers in B and C
        while i < n1:
            A[k]=B[i]
            i=i+1
            k=k+1

        while j < n2:
            A[k]=C[j]
            j=j+1
            k=k+1
            
            
if __name__ == '__main__':  
    
    # Ask for input a list of numbers
    print('Please input a list of numbers separated by comma: ')
    
    # Read from stdin 
    alist = sys.stdin.readline()

    # convert to integer list
    alist = list(map(int,alist.split(','))) 
    
    # Print the input
    print('The list before mergesort is: ')
    print(alist)
    # Call the function
    MergeSort(alist)
    # Print the result
    print('The list after mergesort is: ')
    print(alist)
    