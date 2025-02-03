# Lower Bound -> a[index] >= x
#Lower Bound: Finds the first position in a sorted array where 
# the target can be inserted without violating the order 
# (i.e., the smallest index where the element is greater than or equal to the target).

#Upper Bound -> a[index] > x
#Upper Bound: Finds the first position in a sorted array where 
#the target can no longer be inserted without violating the order 
# (i.e., the smallest index where the element is strictly greater than the target).

def lower_bound(arr, x, n):
    low = 0
    high = n-1
    ans = n

    while(low <= high):
        mid = low + (high-low)//2
        if(arr[mid] >= x):
            #Maybe an answer
            ans = mid
            #Look for more small index on the left
            high = mid-1
        else:
            #Look for small index on right
            low = mid+1
    return ans
#Time Complexity: O(logN), where N = size of the given array.
#Reason: We are basically using the Binary Search algorithm.
#Space Complexity: O(1) as we are using no extra space.
def upper_bound(arr, x, n):
    low = 0
    high = n-1
    ans = n

    while(low <= high):
        mid = low + (high-low)//2
        if(arr[mid] > x):
            #Maybe an answer
            ans = mid
            #Look for more small index on the left
            high = mid-1
        else:
            #Look for small index on right
            low = mid+1
    return ans

arr = [1,2,2,3]
target = int(input("Enter the key (x): "))
ans_l = lower_bound(arr, target, len(arr))
ans_r = upper_bound(arr, target, len(arr))
print(f"Lower bound of {target} is (index): {ans_l}" )
print(f"Upper bound of {target} is (index): {ans_r}" )