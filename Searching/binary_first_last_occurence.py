#TC = O(log2(n) + log2(n)) = O(2log2(n))
#SC = O(1)

def first_occ(arr, n, x):
    low, high = 0, n-1
    first = -1
    while(low <= high):
        mid = low + (high-low)//2
        if(arr[mid] == x):
            first = mid
            high = mid -1
        #move leftward directly
        elif(arr[mid] > x):
            high = mid -1
        #else move rightward
        else:
            low = mid + 1    
    return first

def last_occ(arr, n, x):
    low, high = 0, n-1
    last = -1
    while(low <= high):
        mid = low + (high-low)//2
        if(arr[mid] == x):
            last = mid
            low = mid +1
        #move rightwards directly
        elif(arr[mid] < x):
            low = mid + 1
        #else move leftward
        else:
            high = mid - 1    
    return last


arr = [3, 4, 4, 7, 8, 10]
target = int(input("Enter the key (x): "))
first = first_occ(arr, len(arr), target)

#We check for if the elem is not present, then don't waste 
#another log2(n) time to search for last occurence of elem
if(first == -1):
    print(f"Element not found in the arr")
else:
    print(f"First occurence of {target} is at index: {first}")
    last = last_occ(arr, len(arr),target)
    print(f"Last occurence of {target} is at index: {last}")
