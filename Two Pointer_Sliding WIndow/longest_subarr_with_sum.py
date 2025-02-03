#Longest subarray with sum <= k
#arr = [2, 5, 1, 7, 10], k = 14

#Brute force Approach
#TC = O(n^2)
#Generate all subarr
def long_subarr_with_sum(arr, k):
    '''
    maxlen = 0
    n = len(arr)
    for i in range(n):
        sum = 0
        for j in range(i, n-1):
            sum += arr[j]
            if sum <= k:
                maxlen = max(maxlen, j-1+1)
            #Optimization
            elif(sum > k): break
    return maxlen
    '''

    #Better Approach
    #TC = O(n + n) = O(2n)
    #SC = O(1)
    #r moves n times in worst case
    #In worst possible case we can take out at max n elem while window shrinkage so l moves n times
    '''
    maxlen = 0
    n = len(arr)
    l, r = 0, 0
    start, end = 0, 0  # To store the indices of the maximum length subarray
    sum = 0
    while r < n:
        sum += arr[r]  
        while sum > k: #sum becomes invalid
            sum -= arr[l]
            l += 1 #window shrinkage
        if sum <= k:
            if r-l+1 > maxlen:
                maxlen = r-l+1
                start, end = l, r  # Update the indices
            #Or if we don't want to store the indices then
            #maxlen = max(maxlen, r-l+1) in place of above 3 lines
        r += 1  #window expansion
    return maxlen, start, end
    '''

    #Optimized Approach
    #TC = O(n)
    #SC = O(1)
    maxlen = 0
    n = len(arr)
    l, r = 0, 0
    # To store the indices of the maximum length subarray
    start, end = 0, 0  #Optinal for question specific
    sum = 0
    while r < n:
        sum += arr[r]  
        if sum > k: #we do not shrink the window less than maxlen once found for optimal approach
            sum -= arr[l]
            l += 1 #window shrinkage
        if sum <= k:
            if r-l+1 > maxlen:
                maxlen = r-l+1
                start, end = l, r  # Update the indices
            #Or if we don't want to store the indices then
            #maxlen = max(maxlen, r-l+1) in place of above 3 lines
        r += 1  #window expansion
    return maxlen, start, end

arr = [2, 5, 1, 7, 10]
k = 14
print(long_subarr_with_sum(arr, k))