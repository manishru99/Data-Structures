#Naive approach
#Use linear search
#Tc = O(n)
def occurence_naive(arr, target):
    first, last = -1, -1
    #for i in range(n):
    for index in range(len(arr)):
        if(arr[index] == target):
            # Value occurs for the 1st time
            if(first == -1):
                first = last = index
            else:
                last = index

    return first, last

#TC = O(log2(n) + log2(n)) = O(2log2(n))
#SC = O(1)
def occurence_optimized(arr, n, target):
    #Find lower bound for first occurence arr[ind] >= x
    #Find upper bound - 1 for the last occurence arr[ind] >x
    lb = lower_bound(arr, target, n)
    #lb == n -> lb not present ie elem not present 
    #arr[lb] != target -> lb will point to an index where
    #arr[ind] >= target so we check this condition
    if(lb == n or arr[lb] != target):
        return -1, -1
    return (lb, upper_bound(arr, target, n) - 1)


def lower_bound(arr, x, n):
    low = 0
    high = n-1
    ans = n

    while(low <= high):
        mid = low + (high-low)//2
        if(arr[mid] >= x):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

def upper_bound(arr, x, n):
    low = 0
    high = n-1
    ans = n
    while(low <= high):
        mid = low + (high-low)//2
        if(arr[mid] > x):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans
            

arr = [3, 4, 4, 4, 7, 8, 10]
target = int(input("Enter the key (x): "))
#first, last = occurence_naive(arr, target)
first, last = occurence_optimized(arr, len(arr),target)
print(f"First occurence of {target} is at index: {first}")
print(f"Last occurence of {target} is at index: {last}")
