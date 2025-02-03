#The floor of x is the largest element in the array which is smaller than or equal to x.
#Largest elem <= x

#The ceiling of x is the smallest element in the array greater than or equal to x.
#ceiling of x is basically the LOWER BOUND of x (smallest elem >= x)

def find_ceil(arr, x, n):
    low = 0
    high = n-1
    ans = -1

    while(low <= high):
        mid = low + ( high - low)//2
        if(arr[mid] >= x):
            #Maybe an answer
            ans = arr[mid]
            #Look for more small index on the left
            high = mid-1
        else:
            #Look for small index on right
            low = mid+1
    return ans

def find_floor(arr, x, n):
    low = 0
    high = n-1
    ans = -1

    while(low <= high):
        mid = low + ( high - low)//2
        if(arr[mid] <= x):
            #Maybe an answer
            ans = arr[mid]
            
            low = mid + 1
        else:
            
            high = mid - 1
    return ans

arr = [3, 4, 4, 7, 8, 10]
target = int(input("Enter the key (x): "))
ans_l = find_ceil(arr, target, len(arr))
ans_r = find_floor(arr, target, len(arr))
print(f"Ceil of {target} is: {ans_l}" )
print(f"Floor of {target} is: {ans_r}" )