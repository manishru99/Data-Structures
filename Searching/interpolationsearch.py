#The Interpolation Search is an improvement over Binary Search for instances, where the values in a sorted array are uniformly distributed.

#Time Complexity: O(log2(log2 n)) for the average case, and O(n) for the worst case 
#Auxiliary Space Complexity (recursive): O(n) 
#Auxiliary Space Complexity (iteraative): O(1)
#pos = low + ((high - low) // (arr[high] - arr[low]) *
#                   (x - arr[low]))

#Recursive approach
def interpolationSearch(arr, low, high, x):
    if(low<=high and x>=arr[low] and x<=arr[high]):
        # Probing the position with keeping
        # uniform distribution in mind.
        #pos = low + ((x - arr[low])*(high-low)// arr[high] - arr[low]) 
        pos = low + ((high - low) // (arr[high] - arr[low]) *
                    (x - arr[low]))
        #Base condition
        if(arr[pos] == x):
            return pos
        # If x is smaller, x is in left subarray
        if(arr[pos] > x):
            return interpolationSearch(arr, low, pos-1, x)
        # If x is larger, x is in right subarray
        if(arr[pos]< x):
            return interpolationSearch(arr, pos+1, high, x)
        
    return -1

#Iterative approach
def interpolationSearch_iterative(arr, n, x): 
   
    # Find indexes of two corners 
    low = 0
    high = (n - 1) 
   
    # Since array is sorted, an element present 
    # in array must be in range defined by corner 
    while low <= high and x >= arr[low] and x <= arr[high]: 
        if low == high: 
            if arr[low] == x: 
                return low; 
            return -1; 
   
        # Probing the position with keeping 
        # uniform distribution in mind. 
        pos = int(low + (((float(high - low)/( arr[high] - arr[low])) * (x - arr[low])))) 
   
        # Condition of target found 
        if arr[pos] == x: 
            return pos 
   
        # If x is larger, x is in upper part 
        if arr[pos] < x: 
            low = pos + 1; 
   
        # If x is smaller, x is in lower part 
        else: 
            high = pos - 1; 
       
    return -1


# Array of items in which
# search will be conducted
arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
 
# Element to be searched
x = 18
index = interpolationSearch(arr, 0, n - 1, x)
index1 = interpolationSearch_iterative(arr, n, x)
 
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")

if index1 != -1:
    print("Element found at index (iterative)", index)
else:
    print("Element not found (iterative)")