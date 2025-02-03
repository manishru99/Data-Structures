#Count occurences of 'x' in a sorted array.
#eg. [1,1,1,2,2,3,3], x=3, o/p = 2

#Naive approach
#Use linear search
#Tc = O(n)

#TC = O(log2(n) + log2(n)) = O(2log2(n))
#SC = O(1)
def count_occurence(arr, n, target):
    lb = lower_bound(arr, target, n)
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
first, last = count_occurence(arr, len(arr),target)
print(f"Total number of occurences of {target} is: {last - first + 1}")

