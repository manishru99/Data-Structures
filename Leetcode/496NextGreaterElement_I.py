def next_greater_element(nums1, nums2):
    #Create a dictionary next_great to store the NGE for each number in nums2 for constant-time lookup. O(1)
    #Hashing
    next_greater = {}
    stack = []

    # Iterate through nums2 in reverse order
    for num in reversed(nums2):
        # Maintain a decreasing stack
        while stack and stack[-1] <= num:
            stack.pop()
        # If stack is not empty, the top element is the next greater element
        if stack:
            next_greater[num] = stack[-1]  #Update dict
        else:
            next_greater[num] = -1         #Update dict
        # Push the current element onto the stack
        stack.append(num)

    # Create the result array for nums1 based on the next greater elements found in nums2
    result = [next_greater[num] for num in nums1]

    return result

# Example usage
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(next_greater_element(nums1, nums2))  # Output: [-1, 3, -1]


#TC = O(nums1.length + nums2.length)


'''
def next_greater_element_brute_force(nums1, nums2):
    result = []
    for num1 in nums1:
        found = False
        for i in range(len(nums2)):
            if nums2[i] == num1:
                for j in range(i + 1, len(nums2)):
                    if nums2[j] > num1:
                        result.append(nums2[j])
                        found = True
                        break
                if not found:
                    result.append(-1)
                break
    return result

# Example usage
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(next_greater_element_brute_force(nums1, nums2))  # Output: [-1, 3, -1]

TC = O(nums1.length * (nums2.length)^2)
SC = O(nums1.length)
'''