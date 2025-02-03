#Given an array, we have to find the largest element 
# in the array.

def largest_element(arr):
    n = len(arr)
    largest = 0
    pos = 0
    for i in range(n):
        if( arr[i] > largest):
            #If elem is greater than current largest
            #We update largest
            largest = arr[i]
            pos = i
    return largest, pos
#TC = O(n)
#SC = O(1)

#Another solution:
#Sort the given array
#Largest elem will be at last pos
#Largest elem is arr[n-1]
#TC = O(nlogn) Sorting TC
#SC = O(1)

arr = [3,2,1,5,2]
#print(largest_element(arr))
l,pos = largest_element(arr)
print(f"Largest element is {l} at position = {pos+1}")