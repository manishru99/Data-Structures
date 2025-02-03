
def prefixMax(arr):
    # List to store the prefix max
    prefix_max_arr = []
    # Variable to keep track of the maximum value so far
    current_max = float('-inf')  # Start with the smallest possible value
    for num in arr:
        # Update the current max if the current number is larger
        current_max = max(current_max, num)
        # Append the current max to the prefix max array
        prefix_max_arr.append(current_max)
    return prefix_max_arr

arr = [2, 1, 0, 5, 3]
print("Input Array:", arr)
print("Prefix Max Array:", prefixMax(arr))

#TC = O(n)

'''
The Prefix Max of an array is a new array where each element at index i represents the maximum value of the input array from index 0 to i. Here's how you can compute it:

Steps:
Initialize an empty list to store the prefix max values.
Iterate through the array while keeping track of the maximum value encountered so far.
For each element, compare it with the maximum value so far, update the maximum, and append it to the prefix max list.
'''