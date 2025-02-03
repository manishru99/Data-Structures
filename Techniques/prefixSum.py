def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    
    # Compute prefix sums
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    
    return prefix

# Query using prefix sum
def range_sum(prefix, l, r):
    if l == 0:
        return prefix[r]
    return prefix[r] - prefix[l-1]

# Example
arr = [2, 4, 6, 8, 10]
prefix = prefix_sum(arr)
print("Prefix sum array:", prefix)
print("Sum of range [1, 3]:", range_sum(prefix, 1, 3))  # Output: 18

'''
What Is a Prefix Sum?
A prefix sum is the cumulative sum of elements in an array up to a given index. For an array arr, the prefix sum at index i is:

prefix_sum[i]=arr[0]+arr[1]+⋯+arr[i]

2. Key Idea
Precompute the prefix sums for the array.
Use the prefix sums to quickly answer range-sum queries (or similar problems) in O(1) time, after an 
O(n) preprocessing step.

3. Steps to Solve Prefix Sum Problems
Step 1: Compute the Prefix Sum Array
For an array arr of size n, the prefix sum array can be computed as:

Initialize prefix_sum[0] = arr[0].
For i=1 to n-1, compute:
prefix_sum[i]= prefix_sum[i-1]+arr[i]

Step 2: Use Prefix Sum for Queries
To find the sum of a subarray from index 

range_sum(l,r)=prefix_sum[r] - prefix_sum[l-1]
If l=0, then:
range_sum(0,r)=prefix_sum[r]

'''