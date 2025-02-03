import math
#Requires a sorted array

def jumpSearch(arr, x, n):
    step = math.sqrt(n)

    prev=0
    #As step can go greater than size(n) so min(step,n)
    #-1 for arr index for position
    #Jump through the arr to find the block containing the target
    while(prev < n and arr[int(min(step,n)-1)] < x):
        prev = step
        step += math.sqrt(n)
        if(prev>=n):    #Target not present
            return -1
    
    while(arr[int(prev)] < x):
        prev+=1

        if(prev == min(step,n)):
            return -1
    
    if(arr[int(prev)]== x):
        return prev

    return -1

#TC = O(sqrt(n))

#The total number of comparisons in the worst case is the sum of:
# 1.The jump steps: (n/m)
# 2. The linear search steps (m)
#T(n) = n/m +m
#differentiate on both sides to get m=sqrt(n)
#T(n)= n/sqrt(n) + n
#T(n)= 2(sqrt(n))
#T(n)= O(sqrt(n))


#SC =O(1)

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
x = 55
n = len(arr)
 
# Find the index of 'x' using Jump Search
index = jumpSearch(arr, x, n)

print("Number:", x, "is at index","%.0f"%index, "or position", "%.0f"%(index+1))
