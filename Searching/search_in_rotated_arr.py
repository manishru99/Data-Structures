
def search(nums, n, target):
    low = 0
    high = n-1
    while(low <= high):
        mid = low + (high-low)//2
        #If target present at mid
        if(nums[mid] == target):
            return mid
        #Find the sorted part and apply logic
        #left part sorted
        if(nums[low] <= nums[mid]):
            #If the target exists in the left sorted half
            if(nums[low] <= target and target <= nums[mid]):
                #eliminate the right part
                high = mid - 1
            else:
                #eliminate the left part
                low = mid + 1
        #Right part is sorted
        else:
            #If the target exists in the right sorted half
            if(nums[mid] <= target and target <= nums[high]):
                #eliminate the left part
                low = mid + 1
            else:
                #eliminate the right part
                high = mid - 1
    return -1
    

arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
n = 9
k = 1
ans = search(arr, n, k)
if ans == -1:
    print("Target is not present.")
else:
    print("The index is:", ans)

